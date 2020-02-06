import cv2
import numpy as np
from PIL import Image
from turbojpeg import TurboJPEG

jpeg = TurboJPEG()

mean = np.float32(np.array([123.675, 116.28, 103.53]))
std = np.float32(np.array([58.395, 57.12, 57.375]))
target_size = (224, 224)


def _load_big(jpg_file):
    with open(jpg_file, 'rb') as in_file:
        img = jpeg.decode(in_file.read())
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


def _scale_box(box, scale):
    scale = float(scale)
    x1, y1, x2, y2 = box
    return int(x1 * scale + 0.5), int(y1 * scale + 0.5), int(x2 * scale + 0.5), int(y2 * scale + 0.5)


def _normalize(img):
    img = np.float32(img)
    imgmean = np.float64(mean.reshape(1, -1))
    imgstdinv = 1 / np.float64(std.reshape(1, -1))
    arr = cv2.multiply(cv2.subtract(img, imgmean), imgstdinv)
    return arr


def _normalize_slow(img):
    img = np.float32(img)
    arr = (img - mean) / std
    return arr


def opencv(jpg_file, scale):
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
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = _normalize_slow(img)
    # 6. transpose
    img = img.transpose(2, 0, 1)
    return img


def opencv_fast(jpg_file, scale):
    # 1. load
    img = _load_big(jpg_file)
    # 2. resize
    newsize = _scale_size(img.shape, scale)
    img = cv2.resize(img, newsize, interpolation=cv2.INTER_LINEAR)
    # 3. crop
    x1, y1, x2, y2 = _crop_box(img.shape)
    img = img[y1:y2, x1:x2, ...]
    # 4. flip
    img = np.flip(img, axis=1)
    # 5. normalize
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = _normalize(img)
    # 6. transpose
    img = img.transpose(2, 0, 1)
    return img


def pil(jpg_file, scale):
    # 1. load
    im = Image.open(jpg_file)
    # 2. resize
    newsize = _scale_size(((im.height, im.width)), scale)
    im = im.resize(newsize, Image.BILINEAR)
    # 3. crop
    box = _crop_box((im.height, im.width))
    im = im.crop(box)
    # 4. flip
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    # 5. normalize
    i = np.asarray(im)
    i = _normalize(i)
    # 6. transpose
    i = i.transpose(2, 0, 1)
    return i


def pil_fast(jpg_file, scale):
    # 1. load
    im = Image.open(jpg_file)
    newsize = _scale_size((im.height, im.width), scale)
    box = _crop_box((newsize[1], newsize[0]))
    boxsmall = _scale_box(box, 1 / scale)
    # 3. crop
    im = im.crop(boxsmall)
    # 2. resize
    im = im.resize(target_size, Image.BILINEAR)
    # 4. flip
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    # 5. normalize
    i = np.asarray(im)
    i = _normalize(i)
    # 6. transpose
    i = i.transpose(2, 0, 1)
    return i
