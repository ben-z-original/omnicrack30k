import cv2
import json
import scipy.io
import numpy as np
import fiftyone as fo
from pathlib import Path
from omnicrack30k.importers.base import (
    StructuralDefectsCustomImporter, clear_datasets, launch_fiftyone,
    export2omnicrack30k, cli_arguments_parser)


class CFDImporter(StructuralDefectsCustomImporter):
    def __init__(self, args):
        super().__init__(args.dataset_dir)

        self.dataset_info["year"] = "2015"
        self.dataset_info["Link"] = "https://github.com/cuilimeng/CrackForest-dataset"
        self.dataset_info["reference"] = """
            @article{shi2016automatic,
              title={Automatic road crack detection using random structured forests},
              author={Shi, Yong and Cui, Limeng and Qi, Zhiquan and Meng, Fan and Chen, Zhensong},
              journal={IEEE Transactions on Intelligent Transportation Systems},
              volume={17},
              number={12},
              pages={3434--3445},
              year={2016},
              publisher={IEEE}
            }
            
            @inproceedings{cui2015pavement,
              title={Pavement Distress Detection Using Random Decision Forests},
              author={Cui, Limeng and Qi, Zhiquan and Chen, Zhensong and Meng, Fan and Shi, Yong},
              booktitle={International Conference on Data Science},
              pages={95--102},
              year={2015},
              organization={Springer}
            }"""

    def setup(self):
        with open(str(Path(__file__).parents[3] / "checksums_images.json"), "r") as f:
            splits_dict = json.load(f)

        splits = {
            "train": [key[4:] for key in splits_dict["training"].keys() if key.startswith("CFD_")],
            "validation": [key[4:] for key in splits_dict["validation"].keys() if key.startswith("CFD_")],
            "test": [key[4:] for key in splits_dict["test"].keys() if key.startswith("CFD_")]
        }

        for mode in self.modes:
            files = [(args.dataset_dir / "image" / fname).with_suffix(".jpg")
                     for fname in splits[mode]]

            for f in files[:self.max_samples]:
                sample = fo.Sample(filepath=str(f))

                lab_path = str(f.with_suffix(".mat")).replace("image", "groundTruth")
                lab = scipy.io.loadmat(lab_path)["groundTruth"][0][0][0]
                lab = np.uint8(lab == 2)

                sample = self.prepare_labels(sample, lab)
                sample["tags"] = (mode,)

                self.samples.append(sample)


def main(args):
    clear_datasets()
    dataset_importer = CFDImporter(args)
    fo_dataset = fo.Dataset.from_importer(dataset_importer, name="CFD")

    export2omnicrack30k(fo_dataset, export_dir=args.export_dir)

    if args.visualize:
        session = launch_fiftyone(fo_dataset)
        session.wait()


if __name__ == "__main__":
    parser = cli_arguments_parser()
    parser.add_argument('-d', '--dataset_dir', type=Path,
                        default=Path(__file__).absolute().parents[1] / "subsets" / "cfd",
                        help='Path to root directory of data subset.')
    args = parser.parse_args()
    main(args)
