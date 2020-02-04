import cv2
import numpy as np
from cvbenchmark import jpg_file

img = cv2.imread(jpg_file)


def check(arr):
    assert arr.dtype == np.float32


def np_unit8_to_float32_constructor_run():
    arr = np.float32(img)
    check(arr)


def np_unit8_to_float32_astype_run():
    arr = img.astype('float32')
    check(arr)
