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
    assert np.allclose(arr, run_np())


def run_np():
    arr = (img - mean) / std
    return arr


def run_cv2_div():
    imgmean = np.float64(mean.reshape(1, -1))
    imgstd = np.float64(std.reshape(1, -1))
    arr = cv2.divide(cv2.subtract(img, imgmean), imgstd)
    return arr


def run_cv2_mult():
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    arr = cv2.multiply(cv2.subtract(img, imgmean), imgstdinv)
    return arr
