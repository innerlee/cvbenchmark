import cv2
import numpy as np

from .consts import jpg_file_big

imgs = cv2.imread(jpg_file_big)


def check(img):
    img == (600, 800, 3)


def run_resize():
    rimgs = cv2.resize(imgs, (800, 600), interpolation=cv2.INTER_LINEAR)
    return rimgs


def run_copy():
    rimgs = cv2.copyMakeBorder(imgs, 0, 0, 0, 0, cv2.BORDER_REPLICATE)
    return rimgs
