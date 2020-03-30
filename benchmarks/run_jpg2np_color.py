import cv2
import numpy as np
from turbojpeg import TurboJPEG, TJCS_RGB
import tensorflow as tf

from .consts import jpg_file

jpeg = TurboJPEG()


def check(img):
    assert isinstance(img, np.ndarray)
    assert img.shape == (300, 400, 3)
    assert img.dtype == np.uint8
    assert (img[0, 0] == [5, 3, 4]).all()
    assert (img == run_opencv()).all()


def run_opencv():
    img = cv2.imread(jpg_file, flags=cv2.IMREAD_COLOR)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    return img


def run_turbojpeg():
    with open(jpg_file, 'rb') as in_file:
        img = jpeg.decode(in_file.read(), pixel_format=TJCS_RGB)
    return img


def run_tf():
    with open(jpg_file, 'rb') as in_file:
        img = np.asarray(memoryview(tf.io.decode_jpeg((in_file.read()), dct_method='INTEGER_ACCURATE')))
    return img
