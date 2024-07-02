import cv2
import gdown
import zipfile
import numpy as np
import fiftyone as fo
from pathlib import Path
from omnicrack30k.importers.base import StructuralDefectsCustomImporter, clear_datasets, launch_fiftyone, \
    export2omnicrack30k, cli_arguments_parser


class S2DSImporter(StructuralDefectsCustomImporter):
    def __init__(self, args):
        super().__init__(args.dataset_dir)

        self.dataset_info["year"] = "2022"
        self.dataset_info["Link"] = "https://github.com/ben-z-original/s2ds"
        self.dataset_info["reference"] = """
                @inproceedings{benz2022image,
                  title={Image-Based Detection of Structural Defects Using Hierarchical Multi-scale Attention},
                  author={Benz, Christian and Rodehorst, Volker},
                  booktitle={DAGM German Conference on Pattern Recognition},
                  pages={337--353},
                  year={2022},
                  organization={Springer}
                }"""

        if not args.dataset_dir.exists():
            zip_path = args.dataset_dir.with_suffix(".zip")
            url = "https://drive.google.com/uc?id=1PQ50QKfy2vnDOHSmw5bpBFi33hZsSXuM"
            gdown.download(url, str(zip_path), quiet=False)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(args.dataset_dir)

    def setup(self):
        map_dir_names = {
            "train": "train",
            "validation": "val",
            "test": "test"
        }

        for mode in self.modes:
            files = sorted((Path(self.dataset_dir) / map_dir_names[mode]).glob("*[0-9].png"))

            for f in files[:self.max_samples]:
                sample = fo.Sample(filepath=str(f))

                lab_path = str(f).replace(".png", "_lab.png")
                lab = cv2.imread(lab_path, cv2.IMREAD_GRAYSCALE)
                lab = np.uint8(lab == 255)

                sample = self.prepare_labels(sample, lab)
                sample["tags"] = (mode,)

                self.samples.append(sample)


def main(args):
    clear_datasets()
    dataset_importer = S2DSImporter(args)
    fo_dataset = fo.Dataset.from_importer(dataset_importer, name="S2DS")

    export2omnicrack30k(fo_dataset, export_dir=args.export_dir)

    if args.visualize:
        session = launch_fiftyone(fo_dataset)
        session.wait()


if __name__ == "__main__":
    parser = cli_arguments_parser()
    parser.add_argument('-d', '--dataset_dir', type=Path,
                        default=Path(__file__).absolute().parents[1] / "subsets" / "s2ds",
                        help='Path to root directory of data subset.')
    args = parser.parse_args()
    main(args)
