import cv2
import numpy as np
from turbojpeg import TurboJPEG

from .consts import jpg_file

jpeg = TurboJPEG()


def check(img):
    assert isinstance(img, np.ndarray)
    assert img.shape == (300, 400, 3)
    assert all(img[0, 0] == [4, 3, 5])


def run_opencv():
    img = cv2.imread(jpg_file)
    check(img)


def run_turbojpeg():
    with open(jpg_file, 'rb') as in_file:
        img = jpeg.decode(in_file.read())
    check(img)
