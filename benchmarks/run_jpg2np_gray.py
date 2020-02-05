import cv2
import numpy as np
from turbojpeg import TJPF_GRAY, TurboJPEG

from .consts import jpg_gray_file

jpeg = TurboJPEG()


def check(img):
    assert isinstance(img, np.ndarray)
    assert img.shape == (300, 400)
    assert img.dtype == np.uint8
    assert (img[0, :3] == [4, 3, 2]).all()
    assert (img == run_opencv()).all()


def run_opencv():
    img = cv2.imread(jpg_gray_file, flags=cv2.IMREAD_GRAYSCALE)
    return img


def run_turbojpeg():
    with open(jpg_gray_file, 'rb') as in_file:
        img = jpeg.decode(in_file.read(), pixel_format=TJPF_GRAY)
    return img[:, :, 0]
