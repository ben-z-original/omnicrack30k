import cv2
import json
import numpy as np
import fiftyone as fo
from pathlib import Path
from omnicrack30k.importers.base import (
    StructuralDefectsCustomImporter, clear_datasets, launch_fiftyone,
    export2omnicrack30k, cli_arguments_parser)


class MasonryImporter(StructuralDefectsCustomImporter):
    def __init__(self, args):
        super().__init__(args.dataset_dir)

        self.dataset_info["year"] = "2021"
        self.dataset_info["Link"] = "https://github.com/dimitrisdais/crack_detection_CNN_masonry"
        self.dataset_info["reference"] = """
            @article{Dais2021,  
              author = {Dais, Dimitris and Bal, İhsan Engin and Smyrou, Eleni and Sarhosis, Vasilis},  
              doi = {10.1016/j.autcon.2021.103606},  
              journal = {Automation in Construction},  
              pages = {103606},  
              title = {{Automatic crack classification and segmentation on masonry surfaces using convolutional neural networks and transfer learning}},  
              url = {https://linkinghub.elsevier.com/retrieve/pii/S0926580521000571},  
              volume = {125},  
              year = {2021}  
            }"""

    def setup(self):
        with open(str(Path(__file__).parents[3] / "checksums_images.json"), "r") as f:
            splits_dict = json.load(f)

        splits = {
            "train": [key[8:] for key in splits_dict["training"].keys() if key.startswith("Masonry_")],
            "validation": [key[8:] for key in splits_dict["validation"].keys() if key.startswith("Masonry_")],
            "test": [key[8:] for key in splits_dict["test"].keys() if key.startswith("Masonry_")]
        }

        for mode in self.modes:
            files = [(args.dataset_dir / "dataset" / "crack_detection_224_images" / fname).with_suffix(".png")
                     for fname in splits[mode]]

            for f in files[:self.max_samples]:
                sample = fo.Sample(filepath=str(f))

                lab_path = str(f).replace("_images", "_masks")
                lab = cv2.imread(lab_path, cv2.IMREAD_GRAYSCALE)
                lab = np.uint8(np.where(128 < lab, 1, 0))

                sample = self.prepare_labels(sample, lab)
                sample["tags"] = (mode,)

                self.samples.append(sample)


def main(args):
    clear_datasets()
    dataset_importer = MasonryImporter(args)
    fo_dataset = fo.Dataset.from_importer(dataset_importer, name="Masonry")

    export2omnicrack30k(fo_dataset, export_dir=args.export_dir)

    if args.visualize:
        session = launch_fiftyone(fo_dataset)
        session.wait()


if __name__ == "__main__":
    parser = cli_arguments_parser()
    parser.add_argument('-d', '--dataset_dir', type=Path,
                        default=Path(__file__).absolute().parents[1] / "subsets" / "masonry",
                        help='Path to root directory of data subset.')
    args = parser.parse_args()
    main(args)
