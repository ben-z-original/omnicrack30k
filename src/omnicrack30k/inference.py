import cv2
import torch
import gdown
import zipfile
import numpy as np
import gradio as gr
from pathlib import Path
from argparse import ArgumentParser
from skimage.morphology import thin
from torchvision.transforms import Normalize
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor


class OmniCrack30kModel:
    def __init__(self, planpath=None, folds=(0,1,2,4), allow_tqdm=True,
                 url="https://drive.google.com/uc?id=15S1dvjr7050kISlQ0JTiEPA1eeUDfoOl"):
        # instantiate the nnUNetPredictor
        self.predictor = nnUNetPredictor(
            tile_step_size=0.5,
            use_gaussian=True,
            use_mirroring=True,
            perform_everything_on_device=True,
            device=torch.device('cuda', 0) if torch.cuda.is_available() else torch.device('cpu'),
            verbose=False,
            verbose_preprocessing=False,
            allow_tqdm=allow_tqdm,
        )

        if planpath is None:
            planpath = Path(__file__).parent / "checkpoints" / "nnUNetTrainer__nnUNetPlans__2d"

        # doẃnload and unzip plan
        zippath = Path(planpath).with_suffix(".zip")
        if not zippath.exists() and not Path(planpath).exists():
            Path(planpath.parent).mkdir(exist_ok=True)
            gdown.download(url, str(zippath), quiet=False)

        if not Path(planpath).exists():
            with zipfile.ZipFile(str(zippath), 'r') as zip_ref:
                zip_ref.extractall(str(planpath))

        # initializes the network architecture, loads the checkpoint
        self.predictor.initialize_from_trained_model_folder(
            str(planpath),
            use_folds=folds,
            checkpoint_name='checkpoint_final.pth',
        )

        self.predictor.network.eval()
        self.preprocessor = self.predictor.configuration_manager.preprocessor_class()

        # the follwing attributes are only relevant for the crackstructures multiview approach
        # https://github.com/ben-z-original/crackstructures
        self.classes = ["background", "crack"]
        self.class_weight = torch.tensor([1, 10], dtype=torch.float16)

    def __call__(self, img, rgb=False):
        # prepare image
        img = torch.tensor(img, dtype=torch.float32)
        img = img.moveaxis(-1, 0) if img.shape[0] != 3 else img
        img[:, torch.all(img == 0, dim=0)] = \
            torch.rand_like(img)[:, torch.all(img == 0, dim=0)]  # avoid patches of all zeros

        # transform image
        img = img[[2, 1, 0], ...] if rgb else img
        data = Normalize(img.mean((1, 2)), img.std((1, 2)))(img)
        data = data.unsqueeze(1)

        # run segmentation
        logits = self.predictor.predict_logits_from_preprocessed_data(data).squeeze().cpu()
        softmax = torch.nn.functional.softmax(logits.to(torch.float32), dim=0)
        argmax = torch.argmax(logits, dim=0).to(torch.uint8)

        return softmax, argmax

    def predict_np(self, img, vis=False, rgb=False):
        softmax, argmax = self.__call__(img, rgb=rgb)

        # prepare outputs
        softmax = softmax[self.classes.index("crack")].numpy()
        argmax = 255 * argmax.numpy()

        # compute centerlines
        centerlines = np.uint8(255 * thin(argmax))

        # invert for visualization
        softmax = 1 - softmax
        argmax = 255 - argmax
        centerlines = 255 - centerlines

        if vis:
            # needed because nnunet enforces non-gui backend
            import matplotlib
            matplotlib.use("TkAgg")
            from matplotlib import pyplot as plt

            plt.subplot(221)
            plt.imshow(img)
            plt.title("Input Image")
            plt.subplot(222)
            plt.imshow(softmax, 'gray')
            plt.title("Softmax")
            plt.subplot(223)
            plt.imshow(argmax, 'gray')
            plt.title("Argmax")
            plt.subplot(224)
            plt.imshow(centerlines, 'gray')
            plt.title("Centerlines")
            plt.tight_layout()
            plt.show()

        return softmax, argmax, centerlines

    def nnunet_preprocessing(self, imgpath):
        data, _, _ = self.preprocessor.run_case([imgpath],
                                                None,
                                                self.predictor.plans_manager,
                                                self.predictor.configuration_manager,
                                                self.predictor.dataset_json)
        return data


def main(predictor, title, description):
    parser = ArgumentParser(description="""Start a local gradio app for crack segmentation
                                            or run on segmentation on provided filepath(s).""")
    parser.add_argument('path', nargs='?', default=None, help="Path to image or folder to be processes")
    parser.add_argument('-nv', '--no_vis', action="store_false", help="Turn off visualization for image")
    args = parser.parse_args()

    if args.path is None:
        demo = gr.Interface(fn=predictor.predict_np,
                            title=title,
                            description=description,
                            inputs=gr.Image(label="Input Image"),
                            outputs=[gr.Image(label="Softmax"),
                                     gr.Image(label="Argmax"),
                                     gr.Image(label="Centerlines")])
        demo.launch()
    else:
        path = Path(args.path)

        paths = [path] if path.is_file() else sorted(path.glob("*"))
        for p in paths:
            img = cv2.imread(str(p), cv2.IMREAD_COLOR)
            predictor.predict_np(img, vis=args.no_vis)


if __name__ == "__main__":
    predictor = OmniCrack30kModel()
    title = "OmniCrack30k Crack Segmentation"
    description = """
        Official model trained on the OmniCrack30k crack segmentation dataset. 
        For details kindly refer to https://github.com/ben-z-original/omnicrack30k 
        and the corresponding [publication](https://openaccess.thecvf.com/content/CVPR2024W/VAND/papers/Benz_OmniCrack30k_A_Benchmark_for_Crack_Segmentation_and_the_Reasonable_Effectiveness_CVPRW_2024_paper.pdf).
        To limit runtime and computation resources, this demo runs on a single fold 
        (not the ensemble), which slightly reduces performance.
        """
    main(predictor, title, description)
