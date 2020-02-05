import numpy as np

bboxes = np.array([
    [100, 100, 200, 200],
    [-10, 100, 90, 200],
    [100, -10, 200, 90],
    [310, 100, 410, 200],
    [100, 210, 200, 310],
])
img_shape = (300, 400)


def check(box):
    assert box.shape == bboxes.shape
    assert box.dtype == bboxes.dtype
    assert (box == np.array([[100, 100, 200, 200], [0, 100, 90, 200], [100, 0, 200, 90], [310, 100, 399, 200],
                             [100, 210, 200, 299]])).all()


def run_fast():
    cmin = np.empty(bboxes.shape[-1], dtype=bboxes.dtype)
    cmin[..., 0::2] = img_shape[1] - 1
    cmin[..., 1::2] = img_shape[0] - 1
    clipped_bboxes = np.maximum(np.minimum(bboxes, cmin), 0)
    check(clipped_bboxes)


def run_clip():
    cmin = np.empty(bboxes.shape[-1], dtype=bboxes.dtype)
    cmin[..., 0::2] = img_shape[1] - 1
    cmin[..., 1::2] = img_shape[0] - 1
    clipped_bboxes = np.clip(bboxes, 0, cmin)
    check(clipped_bboxes)


def run_slow():
    clipped_bboxes = np.empty_like(bboxes, dtype=bboxes.dtype)
    clipped_bboxes[..., 0::2] = np.maximum(np.minimum(bboxes[..., 0::2], img_shape[1] - 1), 0)
    clipped_bboxes[..., 1::2] = np.maximum(np.minimum(bboxes[..., 1::2], img_shape[0] - 1), 0)
    check(clipped_bboxes)
