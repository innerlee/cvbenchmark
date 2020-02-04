import cv2
import numpy as np
from cvbenchmark import jpg_file

imgs = [np.float32(cv2.imread(jpg_file)).transpose(2, 0, 1) for i in range(64)]


def check(arr):
    assert arr.shape == (64, 3, 300, 400)


def img_list_stack_constructor_run():
    arr = np.array(imgs)
    check(arr)


def img_list_stack_stack_run():
    arr = np.stack(imgs, axis=0)
    check(arr)
