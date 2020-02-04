# CV Benchmark

Who is fast, and who is the fastest.

## Results

- Read a `.jpeg` image as an numpy array.

```bash
# opencv
python -m timeit "import cvbenchmark as cb; cb.jpg2np_opencv_run()"
# 200 loops, best of 5: 1.48 msec per loop

# PyTurboJPEG (libjpeg-turbo), https://pypi.org/project/PyTurboJPEG/
python -m timeit "import cvbenchmark as cb; cb.jpg2np_turbojpeg_run()"
# 500 loops, best of 5: 631 usec per loop
```

## Development Guide

```bash
# install formatter
pip install yapf

# install pre-commit tool
pip install pre-commit
pre-commit install

# manually check all files
pre-commit run --all-files
```

## Install

```bash
# for development
python setup.py develop

# for deploy
python setup.py install
```
