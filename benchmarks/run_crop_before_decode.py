import cv2
from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE
from .consts import jpg_file
jpeg = TurboJPEG()
in_file = open(jpg_file, 'rb')
data = in_file.read()
in_file.close()


def check(img):
    img == (224, 224, 3)


def run_full():
    img = jpeg.decode(data)[16:(16 + 224), 16:(16 + 224)]
    return img


def run_partial():
    img = jpeg.decode(jpeg.crop(data, 16, 16, 224, 224))
    return img
