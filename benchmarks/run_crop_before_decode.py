import os

import numpy as np
import tensorflow as tf
from turbojpeg import TurboJPEG

from .consts import jpg_file

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

jpeg = TurboJPEG()
in_file = open(jpg_file, 'rb')
data = in_file.read()
in_file.close()


def check(img):
    img == (224, 224, 3)
    print(img[44, 44])


def run_full():
    img = jpeg.decode(data)[16:(16 + 224), 16:(16 + 224)]
    return img


def run_partial():
    img = jpeg.decode(jpeg.crop(data, 16, 16, 224, 224))
    return img


def run_tf():
    img = tf.reverse(tf.io.decode_and_crop_jpeg(tf.convert_to_tensor(data), (16, 16, 224, 224)), [-1]).numpy()
    return img


def run_tf_noreverse():
    img = tf.io.decode_and_crop_jpeg(tf.convert_to_tensor(data), (16, 16, 224, 224)).numpy()
    return img


def run_tf_noreverse_view():
    img = np.asarray(memoryview(tf.io.decode_and_crop_jpeg(tf.convert_to_tensor(data), (16, 16, 224, 224))))
    return img
