import cv2
import numpy as np
import fiftyone as fo
from pathlib import Path
from omnicrack30k.importers.base import StructuralDefectsCustomImporter, clear_datasets, launch_fiftyone, \
    export2omnicrack30k, cli_arguments_parser


class CeramicImporter(StructuralDefectsCustomImporter):
    def __init__(self, args):
        super().__init__(args.dataset_dir)

        self.dataset_info["year"] = "2021"
        self.dataset_info["Link"] = "https://github.com/gerivansantos/ceramic-cracks-dataset"
        self.dataset_info["reference"] = """
            @article{junior2021ceramic,
              title={Ceramic cracks segmentation with deep learning},
              author={Junior, Gerivan Santos and Ferreira, Janderson and Mill{\'a}n-Arias, Cristian and Daniel, Ramiro and Junior, Alberto Casado and Fernandes, Bruno JT},
              journal={Applied Sciences},
              volume={11},
              number={13},
              pages={6017},
              year={2021},
              publisher={MDPI}
            }"""

    def setup(self):
        # indices of sorted samples for data split
        val_samples = [4, 9, 12, 15, 30, 36, 47, 49, 64, 67, 83, 87, 91, 96, 97]
        test_samples = [0, 10, 18, 20, 22, 25, 35, 38, 45, 51, 52, 62, 63, 88, 93]

        files = np.array(sorted((Path(self.dataset_dir) / "train" / "image").glob("*")))

        splits = {
            "train": np.delete(files, np.append(val_samples, test_samples)),
            "validation": files[val_samples],
            "test": files[test_samples]
        }

        for mode in self.modes:
            files = splits[mode]

            for f in files[:self.max_samples]:
                sample = fo.Sample(filepath=str(f))

                lab_path = str(f).replace("image", "label")
                lab = cv2.imread(lab_path, cv2.IMREAD_GRAYSCALE)
                lab = np.uint8(np.where(128 < lab, 1, 0))

                sample = self.prepare_labels(sample, lab)
                sample["tags"] = (mode,)

                self.samples.append(sample)


def main(args):
    clear_datasets()
    dataset_importer = CeramicImporter(args)
    fo_dataset = fo.Dataset.from_importer(dataset_importer, name="Ceramic")

    export2omnicrack30k(fo_dataset, export_dir=args.export_dir)

    if args.visualize:
        session = launch_fiftyone(fo_dataset)
        session.wait()


if __name__ == "__main__":
    parser = cli_arguments_parser()
    parser.add_argument('-d', '--dataset_dir', type=Path,
                        default=Path(__file__).absolute().parents[1] / "subsets" / "ceramic",
                        help='Path to root directory of data subset.')
    args = parser.parse_args()
    main(args)
