import cv2
import numpy as np
import torch

from .consts import jpg_file_224

imgs = [cv2.imread(jpg_file_224) for _ in range(8)]
mean = np.float32(np.array([123.675, 116.28, 103.53]))
std = np.float32(np.array([58.395, 57.12, 57.375]))
imgmean_gpu = torch.from_numpy(mean).view(1, 3, 1, 1).to('cuda:0')
imgstd_gpu = torch.from_numpy(std).view(1, 3, 1, 1).to('cuda:0')


def check(arr):
    assert (arr - run_cpu()).abs().sum().cpu().item() == 0


def _cv2_normalize(img):
    img = np.float32(img)
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    arr = cv2.multiply(cv2.subtract(img, imgmean), imgstdinv)
    return arr


def run_cpu():
    img_group = [_cv2_normalize(img) for img in imgs]
    img_group = [img.transpose(2, 0, 1) for img in img_group]
    img_group = np.array(img_group)
    imgs_gpu = torch.from_numpy(img_group).to('cuda:0')
    return imgs_gpu


def run_gpu():
    img_group = [img.transpose(2, 0, 1) for img in imgs]
    img_group = np.array(img_group)
    imgs_gpu = torch.from_numpy(img_group).to('cuda:0').float()
    imgs_gpu = imgs_gpu.sub_(imgmean_gpu)
    imgs_gpu = imgs_gpu.div_(imgstd_gpu)

    return imgs_gpu
