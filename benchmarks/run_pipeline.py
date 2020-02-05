import cv2
import numpy as np
from benchmarks.consts import jpg_file

mean = np.float32(np.array([123.675, 116.28, 103.53]))
std = np.float32(np.array([58.395, 57.12, 57.375]))
scale = np.float32(np.sqrt(2))
scale_small = 1 / scale
target_size = (224, 224)


def check(arr):
    pass


def _load_big():
    img = cv2.imread(jpg_file)
    return img


def _scale_size(size, scale):
    h, w = size[:2]
    return int(w * float(scale) + 0.5), int(h * float(scale) + 0.5)


def _crop_box(size):
    h, w = size[:2]
    tw, th = target_size
    x1 = (w - tw) // 2
    y1 = (h - th) // 2
    box = np.array([x1, y1, x1 + tw, y1 + th])
    return box


def _normalize(img):
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    arr = cv2.multiply(cv2.subtract(img, imgmean), imgstdinv)
    return arr


def run_np():
    # 1. load
    img = cv2.imread(jpg_file)
    # 2. resize
    newsize = _scale_size(img.shape, scale)
    img = cv2.resize(img, newsize, interpolation=cv2.INTER_LINEAR)
    # 3. crop
    x1, y1, x2, y2 = _crop_box(img.shape)
    img = img[y1:y2, x1:x2, ...]
    # 4. flip
    img = np.flip(img, axis=1)
    # 5. normalize
    img = _normalize(img)
    # 6. transpose
    img = img.transpose(2, 0, 1)
    return img
