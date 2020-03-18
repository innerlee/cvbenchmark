import cv2
import numpy as np

from .consts import jpg_file_256

imgs = cv2.imread(jpg_file_256)


def check(img):
    img == (256, 341, 3)


def run_resize():
    rimgs = cv2.resize(imgs, (341, 256), interpolation=cv2.INTER_LINEAR)
    return rimgs


def run_copy():
    rimgs = cv2.copyMakeBorder(imgs, 0, 0, 0, 0, cv2.BORDER_REPLICATE)
    return rimgs
