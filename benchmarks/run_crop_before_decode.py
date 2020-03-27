import cv2
from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

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


def run_tf():
    img = tf.io.decode_and_crop_jpeg(tf.convert_to_tensor(data), (16, 16, 224, 224)).numpy()
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    return img
