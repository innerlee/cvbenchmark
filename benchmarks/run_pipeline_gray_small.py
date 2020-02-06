import numpy as np

from .consts import jpg_gray_file_small
from .pipeline import opencv, opencv_fast, opencv_fastest, pil, pil_fast

scale = np.float32(2.56)


def check(img):
    assert img.shape == (1, 224, 224)
    assert img.dtype == np.float32
    assert np.abs(img - run_opencv()).mean() < 0.05


def run_opencv():
    img = opencv(jpg_gray_file_small, scale, is_gray=True)
    return img


def run_opencv_fast():
    img = opencv_fast(jpg_gray_file_small, scale, is_gray=True)
    return img


def run_opencv_fastest():
    img = opencv_fastest(jpg_gray_file_small, scale, is_gray=True)
    return img


def run_pil():
    img = pil(jpg_gray_file_small, scale, is_gray=True)
    return img


def run_pil_fast():
    img = pil_fast(jpg_gray_file_small, scale, is_gray=True)
    return img
