import numpy as np
from PIL import Image
from turbojpeg import TJCS_RGB, TurboJPEG

from .consts import jpg_file

jpeg = TurboJPEG()


def check(img):
    assert isinstance(img, np.ndarray)
    assert img.shape == (200, 200, 3)
    assert img.dtype == np.uint8


def run_turbojpeg():
    with open(jpg_file, 'rb') as in_file:
        img = jpeg.decode(in_file.read(), pixel_format=TJCS_RGB)
    return img[40:240, 20:220]


def run_PIL():
    img = Image.open(jpg_file).crop((20, 40, 220, 240))

    return np.array(img)
