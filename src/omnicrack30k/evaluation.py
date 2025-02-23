import cv2
import numpy as np
from tqdm import tqdm
from pathlib import Path
from argparse import ArgumentParser
from skimage.morphology import disk
from sklearn.metrics import jaccard_score
from omnicrack30k.inference import OmniCrack30kModel

SUBSETS = {'validation':
               ['BCL', 'Ceramic', 'CFD', 'CRACK500', 'CrackTree260', 'CrSpEE', 'CSSC', 'DeepCrack',
                'DIC', 'GAPS384', 'Khanh11k', 'LCW', 'Masonry', 'S2DS', 'TopoDS', 'UAV75'],
           'test':
               ['AEL', 'BCL', 'Ceramic', 'CFD', 'CRACK500', 'CrackLS315', 'CRKWH100', 'CrSpEE', 'CSSC',
                'DeepCrack', 'DIC', 'GAPS384', 'Khanh11k', 'LCW', 'Masonry', 'S2DS', 'Stone331', 'TopoDS',
                'UAV75']}


def apply_tolerance(true, pred, tol=5):
    true_dil = cv2.dilate(true, disk(tol), iterations=1)
    pred_dil = cv2.dilate(pred, disk(tol), iterations=1)

    # infer true/false positives and negatives
    tp = true * pred_dil
    fp = pred - (pred * true_dil)
    fn = true - tp

    true, pred = tp + fn, tp + fp
    return true, pred


def run_evaluation(datapath, split, subset=None, tolerance=4, planpath=None, folds=(0, 1, 2, 3, 4), texpath=None):
    predictor = OmniCrack30kModel(planpath=planpath, folds=folds, allow_tqdm=False)

    subsets = [subset] if subset is not None else SUBSETS[split]

    trues = {key: np.empty((0,), dtype=bool) for key in subsets}
    preds = {key: np.empty((0,), dtype=bool) for key in subsets}

    tex = ""

    for key in subsets:
        img_paths = (datapath / "images" / split).glob(f"{key}*.png")

        for f in tqdm(list(img_paths)):
            # load image and annotation
            img = cv2.imread(str(f), cv2.IMREAD_COLOR)
            true = cv2.imread(str((datapath / "centerlines" / split / f.name)), cv2.IMREAD_GRAYSCALE)

            # run inference and map classes
            softmax, argmax, centerlines = predictor.predict_np(img)
            true, pred = np.uint8(true == 0), np.uint8(centerlines == 0)

            # some subsets (e.g. Stone331) provide resized masks -> correct that
            if pred.shape != true.shape:
                pred = cv2.resize(pred, (true.shape[1], true.shape[0]), interpolation=cv2.INTER_NEAREST)

            # apply tolerance
            true, pred = apply_tolerance(true, pred, tol=tolerance)
            true, pred = true.flatten(), pred.flatten()

            # remove true negatives (they do not affect IoU)
            keep_idxs = np.where((true == 1) + (pred == 1))[0]
            true, pred = true[keep_idxs], pred[keep_idxs]

            # store results
            trues[key] = np.append(trues[key], true)
            preds[key] = np.append(preds[key], pred)

        # compute centerline IoU (clIoU)
        cliou = jaccard_score(trues[key], preds[key])
        tex += f"& {100 * cliou:.1f} "
        print(f"\n{key}\t{cliou:.3f}")

    if texpath is not None:
        with open(texpath, 'w') as f:
            f.write(tex)


if __name__ == "__main__":
    parser = ArgumentParser(description="""Run evaluation and compute centerline IoU (clIoU).""")
    parser.add_argument('datapath', nargs='?', help="Path to root folder of omnicrack30k dataset.")
    parser.add_argument('split', nargs='?', choices=['test', 'validation'], help="Split for evaluation")
    parser.add_argument('-s', '--subset', type=str, default=None, help="Subset to evaluate.")
    parser.add_argument('-t', '--tolerance', type=int, default=4, help="Tolerance of the clIoU.")
    parser.add_argument('-p', '--planpath', type=str, default=None, help="Path to the plan, i.e. model and weights.")
    parser.add_argument('-f', '--folds', nargs="+", type=int, default=(0, 1, 2, 3, 4), help="Folds for ensemble.")
    parser.add_argument('-tp', '--texpath', type=str, default=None, help="Path to latex output file, if desired.")
    args = parser.parse_args()

    run_evaluation(Path(args.datapath), args.split, args.subset, args.tolerance, args.planpath, args.folds,
                   args.texpath)
