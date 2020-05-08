import glob

from decord import VideoReader, cpu

files = glob.glob('k400/*')


def check(box):
    pass


def run_init():
    for f in files:
        VideoReader(f, ctx=cpu(0))
    return True
