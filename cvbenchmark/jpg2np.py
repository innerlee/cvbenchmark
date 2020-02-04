import cv2
import numpy as np
from cvbenchmark import jpg_file
from turbojpeg import TurboJPEG

jpeg = TurboJPEG()


def check(img):
    assert isinstance(img, np.ndarray)
    assert img.shape == (300, 400, 3)
    assert all(img[0, 0] == [4, 3, 5])


def jpg2np_opencv_run():
    img = cv2.imread(jpg_file)
    check(img)


def jpg2np_turbojpeg_run():
    with open(jpg_file, 'rb') as in_file:
        img = jpeg.decode(in_file.read())
    check(img)
