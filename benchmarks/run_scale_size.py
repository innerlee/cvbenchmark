import numpy as np

img_shape = (300, 400)
scale = np.sqrt(2)


def check(size):
    assert isinstance(size[0], int)
    assert size == (424, 566)


def run_fast():
    w, h = img_shape
    return int(w * float(scale) + 0.5), int(h * float(scale) + 0.5)


def run_round():
    return tuple(np.rint(np.array(img_shape) * scale).astype(int))
