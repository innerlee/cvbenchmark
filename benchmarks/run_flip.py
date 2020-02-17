import cv2
import numpy as np

from .consts import jpg_file_224

imgs = np.array([cv2.imread(jpg_file_224) for _ in range(32)])
imgs2 = imgs.copy()


def check(img):
    assert np.allclose(run_np(), img)


def run_np():
    img = np.flip(imgs, axis=2).copy()
    return img


def run_cv2():
    for i in imgs2:
        cv2.flip(i, 1, i)
    return imgs2
