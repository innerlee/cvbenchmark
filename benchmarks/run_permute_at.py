import cv2
import numpy as np
import torch

from .consts import jpg_file_224

torch.ones(1).to('cuda:0')

imgs = np.array([cv2.imread(jpg_file_224) for _ in range(32)])


def check(imgs_gpu):
    assert np.allclose(np.array(imgs_gpu.shape), np.array([32, 3, 224, 224]))


def run_cpu():
    img = np.array(imgs.transpose(0, 3, 1, 2))
    imgs_gpu = torch.from_numpy(img).to('cuda:0')
    return imgs_gpu


def run_gpu():
    imgs_gpu = torch.from_numpy(imgs).to('cuda:0')
    imgs_gpu = imgs_gpu.permute(0, 3, 1, 2).contiguous()

    return imgs_gpu
