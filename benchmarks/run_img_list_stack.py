import cv2
import numpy as np

from .consts import jpg_file

imgs = [np.float32(cv2.imread(jpg_file)).transpose(2, 0, 1) for i in range(8)]


def check(arr):
    assert arr.shape == (8, 3, 300, 400)


def run_constructor():
    arr = np.array(imgs)
    return arr


def run_stack():
    arr = np.stack(imgs, axis=0)
    return arr
