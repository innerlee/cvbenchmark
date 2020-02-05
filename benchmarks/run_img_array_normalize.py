import cv2
import numpy as np

from .consts import jpg_file

img = np.float32(cv2.imread(jpg_file))
mean = np.float32(np.array([123.675, 116.28, 103.53]))
std = np.float32(np.array([58.395, 57.12, 57.375]))


def check(arr):
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (300, 400, 3)
    assert arr.dtype == np.float32
    assert np.allclose(arr[0, 0], [-2.0494049, -1.9831933, -1.7172985])


def run_np():
    arr = (img - mean) / std
    return arr


def run_cv2_div():
    global mean, std
    mean = np.float64(mean.reshape(1, -1))
    std = np.float64(std.reshape(1, -1))
    arr = cv2.divide(cv2.subtract(img, mean), std)
    return arr


def run_cv2_mult():
    global mean, std
    mean = np.float64(mean.reshape(1, -1))
    stdinv = 1 / np.float64(std.reshape(1, -1))
    arr = cv2.multiply(cv2.subtract(img, mean), stdinv)
    return arr