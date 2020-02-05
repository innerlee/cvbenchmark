import cv2
import numpy as np
from turbojpeg import TJPF_GRAY, TurboJPEG

from .consts import jpg_gray_file

jpeg = TurboJPEG()
with open(jpg_gray_file, 'rb') as in_file:
    imgbytes = in_file.read()


def check(img):
    assert isinstance(img, np.ndarray)
    assert img.shape == (300, 400)
    assert (img[0, :3] == [4, 3, 2]).all()
    assert img.dtype == np.uint8
    assert (img == run_opencv()).all()


def run_opencv():
    img_np = np.frombuffer(imgbytes, np.uint8)
    img = cv2.imdecode(img_np, flags=cv2.IMREAD_GRAYSCALE)
    return img


def run_turbojpeg():
    img = jpeg.decode(imgbytes, pixel_format=TJPF_GRAY)
    return img[:, :, 0]
