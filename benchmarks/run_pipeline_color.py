import numpy as np

from .consts import jpg_file
from .pipeline import opencv, opencv_fast, pil, pil_fast

scale = np.float32(np.sqrt(2))


def check(img):
    assert img.shape == (3, 224, 224)
    assert img.dtype == np.float32
    assert np.abs(img - run_opencv()).mean() < 0.025


def run_opencv():
    img = opencv(jpg_file, scale)
    return img


def run_opencv_fast():
    img = opencv_fast(jpg_file, scale)
    return img


def run_pil():
    img = pil(jpg_file, scale)
    return img


def run_pil_fast():
    img = pil_fast(jpg_file, scale)
    return img
