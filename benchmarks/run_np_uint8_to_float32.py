import cv2
import numpy as np

from .consts import jpg_file

img = cv2.imread(jpg_file)


def check(arr):
    assert arr.dtype == np.float32


def run_constructor():
    arr = np.float32(img)
    return arr


def run_astype():
    arr = img.astype('float32')
    return arr
