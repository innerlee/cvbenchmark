import datetime
import glob

import numpy as np
from decord import VideoReader, cpu

files = glob.glob('k400/*')
# files = glob.glob('k400_32/*')
# files = glob.glob('out*')

init_times = []
decode_times = []


def run():
    for f in files:
        file = open(f, "rb")
        bs = file.read()
        file.close()
        a = datetime.datetime.now()
        with open('/dev/shm/a.mp4', 'wb') as bf:
            bf.write(bs)

        vr = VideoReader('/dev/shm/a.mp4', ctx=cpu(0), num_threads=0)

        a = datetime.datetime.now()
        vr = VideoReader(f, ctx=cpu(0), num_threads=0)
        b = datetime.datetime.now()
        print("init: ", (b - a).microseconds, "us")
        for i in np.array([10, 12, 14, 60, 62, 64]) + 0:
            vr[i]
        c = datetime.datetime.now()
        print(f, "decode: ", (c - b).microseconds, "us")


run()
