# CV Benchmark

Who is fast, and who is the fastest.

## Results

```bash
python -m timeit "import cvbenchmark as cb; cb.jpg2np_opencv_run()"
200 loops, best of 5: 1.52 msec per loop
```

## Usage

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
