import cv2
import numpy as np
import fiftyone as fo
from pathlib import Path
from omnicrack30k.importers.base import StructuralDefectsCustomImporter, clear_datasets, launch_fiftyone, \
    export2omnicrack30k, parse_cli_arguments


class UAV75Importer(StructuralDefectsCustomImporter):
    def __init__(self, args):
        super().__init__(args.dataset_dir)

        self.dataset_info["year"] = "2019"
        self.dataset_info["Link"] = "https://github.com/ben-z-original/uav75"
        self.dataset_info["reference"] = """
            @inproceedings{benz2019crack,
              title={Crack segmentation on UAS-based imagery using transfer learning},
              author={Benz, Christian and Debus, Paul and Ha, Huy Khanh and Rodehorst, Volker},
              booktitle={2019 International Conference on Image and Vision Computing New Zealand (IVCNZ)},
              pages={1--6},
              year={2019},
              organization={IEEE}
            }"""

    def setup(self):
        map_dir_names = {
            "train": "train_img",
            "validation": "val_img",
            "test": "test_img"
        }

        for mode in self.modes:
            files = sorted((Path(self.dataset_dir) / map_dir_names[mode]).glob("*.jpg"))

            for f in files[:self.max_samples]:
                sample = fo.Sample(filepath=str(f))

                lab_path = str(f.with_suffix(".png")).replace("_img", "_lab")
                lab = cv2.imread(lab_path, cv2.IMREAD_GRAYSCALE)
                lab = np.uint8(lab == 255)

                sample = self.prepare_labels(sample, lab)
                sample["tags"] = (mode,)

                self.samples.append(sample)


def main(args):
    clear_datasets()
    dataset_importer = UAV75Importer(args)
    fo_dataset = fo.Dataset.from_importer(dataset_importer, name="UAV75")

    export2omnicrack30k(fo_dataset, export_dir=args.export_dir)

    if args.visualize:
        session = launch_fiftyone(fo_dataset)
        session.wait()


if __name__ == "__main__":
    args = parse_cli_arguments()
    main(args)
