import cv2
import numpy as np
from turbojpeg import TurboJPEG

from .consts import jpg_file

jpeg = TurboJPEG()
with open(jpg_file, 'rb') as in_file:
    imgbytes = in_file.read()


def check(img):
    assert isinstance(img, np.ndarray)
    assert img.shape == (300, 400, 3)
    assert img.dtype == np.uint8
    assert (img[0, 0] == [4, 3, 5]).all()
    assert (img == run_opencv()).all()


def run_opencv():
    img_np = np.frombuffer(imgbytes, np.uint8)
    img = cv2.imdecode(img_np, flags=cv2.IMREAD_COLOR)
    return img


def run_turbojpeg():
    img = jpeg.decode(imgbytes)
    return img
