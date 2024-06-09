import cv2
import json
import hashlib
from pathlib import Path
from PIL import Image


def dump_checksums(dir, outfile):
    files = sorted(Path(dir).glob("**/*.png"))
    checksum_dict = {"training": {}, "validation": {}, "test": {}}
    for f in files:
        key = f.stem
        split = f.parts[-2]
        checksum_dict[split][key] = hashlib.md5(Image.open(f).tobytes()).hexdigest()

        print(key, checksum_dict[split][key])

    with open(outfile, "w") as outfile:
        json.dump(checksum_dict, outfile, indent=2)

def create_directory_structure(trg_root):
    trg_root.mkdir(exist_ok=True)
    (trg_root / "images").mkdir(exist_ok=True)
    (trg_root / "images" / "training").mkdir(exist_ok=True)
    (trg_root / "images" / "validation").mkdir(exist_ok=True)
    (trg_root / "images" / "test").mkdir(exist_ok=True)

    (trg_root / "annotations").mkdir(exist_ok=True)
    (trg_root / "annotations" / "training").mkdir(exist_ok=True)
    (trg_root / "annotations" / "validation").mkdir(exist_ok=True)
    (trg_root / "annotations" / "test").mkdir(exist_ok=True)

if __name__ == "__main__":
    imgs_dir = Path("/media/chrisbe/backup/datasets/omnicrack30k/crackseg/images")
    anno_dir = Path("/media/chrisbe/backup/datasets/omnicrack30k/crackseg/annotations")
    outfile_images = Path("/home/chrisbe/repos/omnicrack30k/checksums_images.json")
    outfile_annotations = Path("/home/chrisbe/repos/omnicrack30k/checksums_annotations.json")

    #dump_checksums(imgs_dir, outfile_images)
    #dump_checksums(anno_dir, outfile_annotations)

    # load checksums
    with open(outfile_images, "r") as json_file:
        checksum_images = json.load(json_file)

    with open(outfile_annotations, "r") as json_file:
        checksum_annotations = json.load(json_file)

    trg_root = Path("/media/chrisbe/backup/datasets/omnicrack30k/tmp/final")
    create_directory_structure(trg_root)

    src_root = Path("/media/chrisbe/backup/datasets/omnicrack30k/tmp")

    #train_samples =

    for mode in ["images"]:
        for f in (src_root / mode).glob("**/*.*"):

            subset = f.parts[-2]
            key = f.stem

            checksum_img = checksum_images[split][f"{subset}_{key}"]
            checksum_img = checksum_images[split][f"{subset}_{key}"]

            #img = cv2.imread(str(f), cv2.IMREAD_COLOR)
            #cv2.imwrite(str((trg_root / mode / split / f"{subset}_{f.stem}").with_suffix(".png")), img)

            print(hashlib.md5(Image.open(f).tobytes()).hexdigest())

            #print(checksum, md5(str(f)))

            print()

    print()
