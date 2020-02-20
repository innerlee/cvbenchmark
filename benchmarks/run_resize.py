import cv2
import numpy as np

from .consts import jpg_file_224

imgs = np.array([cv2.imread(jpg_file_224) for _ in range(32)])


def check(img):
    img == (32, 256, 340, 3)


def run_np():
    rimgs = np.array([cv2.resize(img, (340, 256), interpolation=cv2.INTER_LINEAR) for img in imgs])
    return rimgs


def run_cv2():
    rimgs = np.empty((32, 256, 340, 3), dtype=imgs.dtype)
    for i in range(32):
        cv2.resize(imgs[i], (340, 256), rimgs[i], interpolation=cv2.INTER_LINEAR)
    return rimgs
