import cv2
import numpy as np
import torch
from torchvision.transforms import functional as F

from .consts import jpg_file

image = cv2.imread(jpg_file)
mean = np.float32(np.array([123.675, 116.28, 103.53]))
std = np.float32(np.array([58.395, 57.12, 57.375]))


def check(arr):
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (300, 400, 3)
    assert arr.dtype == np.float32
    assert np.allclose(arr, run_np())


def run_torch():
    img = np.float32(image)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    img = np.transpose(img, [2, 0, 1])
    arr = F.normalize(torch.from_numpy(img), mean=torch.from_numpy(mean), std=torch.from_numpy(std))
    arr = np.transpose(arr, [1, 2, 0]).numpy()
    return arr


def run_np():
    img = np.float32(image)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    arr = (img - mean) / std
    return arr


def run_cv2_div():
    img = np.float32(image)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    imgmean = np.float64(mean.reshape(1, -1))
    imgstd = np.float64(std.reshape(1, -1))
    arr = cv2.divide(cv2.subtract(img, imgmean), imgstd)
    return arr


def run_cv2_mult():
    img = np.float32(image)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    arr = cv2.multiply(cv2.subtract(img, imgmean), imgstdinv)
    return arr


def run_cv2_mult2():
    img = np.float32(image)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    arr = cv2.subtract(img, imgmean)
    cv2.multiply(arr, imgstdinv, arr)
    return arr


def run_cv2_mult3():
    arr = np.float32(image)
    arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    cv2.subtract(arr, imgmean, arr)
    cv2.multiply(arr, imgstdinv, arr)
    return arr


def run_cv2_mult4():
    arr = np.float32(image)
    cv2.cvtColor(arr, cv2.COLOR_BGR2RGB, arr)
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    cv2.subtract(arr, imgmean, arr)
    cv2.multiply(arr, imgstdinv, arr)
    return arr
