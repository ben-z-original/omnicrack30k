import cv2
import torch
import gdown
import zipfile
import numpy as np
import gradio as gr
from pathlib import Path
from argparse import ArgumentParser
from skimage.morphology import thin
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor


class OmniCrack30kModel:
    def __init__(self, planpath=Path(__file__).parent / "checkpoints" / "nnUNetTrainer__nnUNetPlans__2d"):
        # instantiate the nnUNetPredictor
        self.predictor = nnUNetPredictor(
            tile_step_size=0.5,
            use_gaussian=True,
            use_mirroring=True,
            perform_everything_on_device=True,
            device=torch.device('cuda', 0),
            verbose=False,
            verbose_preprocessing=False,
            allow_tqdm=True
        )

        # doẃnload and unzip plan
        zippath = Path(planpath).with_suffix(".zip")
        if not zippath.exists():
            url = "https://drive.google.com/uc?id=1X1NFs4mKPJDBxZZRbiymf6cs_tni1jKg"
            Path(planpath.parent).mkdir(exist_ok=True)
            gdown.download(url, str(zippath), quiet=False)

        if not Path(planpath).exists():
            with zipfile.ZipFile(str(zippath), 'r') as zip_ref:
                zip_ref.extractall(str(planpath))

        # initializes the network architecture, loads the checkpoint
        self.predictor.initialize_from_trained_model_folder(
            str(planpath),
            use_folds=(0,),
            checkpoint_name='checkpoint_final.pth',
        )

        self.preprocessor = self.predictor.configuration_manager.preprocessor_class()

    def __call__(self, img, vis=False, rgb=False):
        # preprocess image
        data_orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) if rgb else img
        data = (data_orig - data_orig.mean((0, 1))) / data_orig.std((0, 1))
        data = torch.tensor(data, dtype=torch.half)
        data = data.moveaxis(-1, 0).unsqueeze(1)

        # run segmentation
        logits = self.predictor.predict_logits_from_preprocessed_data(data).squeeze().cpu()
        softmax = torch.nn.functional.softmax(logits.to(torch.float32), dim=0).numpy()
        argmax = 255 * torch.argmax(logits, dim=0).to(torch.uint8).numpy()
        centerlines = np.uint8(255 * thin(argmax))

        # invert for visualization
        softmax = 1 - softmax
        argmax = 255 - argmax
        centerlines = 255 - centerlines

        if vis:
            plt.subplot(221)
            plt.imshow(data_orig)
            plt.subplot(222)
            plt.imshow(softmax[1], 'gray')
            plt.subplot(223)
            plt.imshow(argmax, 'gray')
            plt.subplot(224)
            plt.imshow(centerlines, 'gray')
            plt.show()

        return softmax[1], argmax, centerlines

    def nnunet_preprocessing(self, imgpath):
        data, _, _ = self.preprocessor.run_case([imgpath],
                                                None,
                                                predictor.plans_manager,
                                                predictor.configuration_manager,
                                                predictor.dataset_json)
        return data


def main():
    parser = ArgumentParser(description="""Start a local gradio app for crack segmentation
                                            or run on segmentation on provided filepath(s).""")
    parser.add_argument('-p', '--path', default=None, help="Path to image or folder to be processes")
    parser.add_argument('-nv', '--no_vis', action="store_false", help="Turn off visualization for image")
    args = parser.parse_args()

    predictor = OmniCrack30kModel()

    if args.path is None:
        demo = gr.Interface(fn=predictor,
                            title="OmniCrack30k Crack Segmentation",
                            description="""
                                Official model trained on the OmniCrack30k crack segmentation dataset. 
                                For details kindly refer to https://github.com/ben-z-original/omnicrack30k 
                                and the corresponding [publication](https://openaccess.thecvf.com/content/CVPR2024W/VAND/papers/Benz_OmniCrack30k_A_Benchmark_for_Crack_Segmentation_and_the_Reasonable_Effectiveness_CVPRW_2024_paper.pdf).
                                To limit runtime and computation resources, this demo runs on a single fold 
                                (not the ensemble), which slightly reduces performance.
                                """,
                            inputs=gr.Image(label="Input Image"),
                            outputs=[gr.Image(label="Softmax"),
                                     gr.Image(label="Argmax"),
                                     gr.Image(label="Centerlines")])
        demo.launch()
    else:
        if args.no_vis:
            # needed because nnunet uses non-gui backend
            import matplotlib

            matplotlib.use("TkAgg")
            from matplotlib import pyplot as plt

        path = Path(args.path)

        paths = [path] if path.is_file() else sorted(path.glob("*"))
        for p in paths:
            img = cv2.imread(str(p), cv2.IMREAD_COLOR)
            predictor(img, vis=args.no_vis)


if __name__ == "__main__":
    main()
