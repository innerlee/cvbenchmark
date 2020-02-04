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

- Image array normalization

```bash
# (img - mean) / std
python -m timeit "import cvbenchmark as cb; cb.img_array_normalize_np_run()"
# 100 loops, best of 5: 2.17 msec per loop

# cv2.divide(cv2.subtract(img, mean), std)
python -m timeit "import cvbenchmark as cb; cb.img_array_normalize_cv2_div_run()"
# 200 loops, best of 5: 1.21 msec per loop

# cv2.multiply(cv2.subtract(img, mean), stdinv)
python -m timeit "import cvbenchmark as cb; cb.img_array_normalize_cv2_mult_run()"
# 200 loops, best of 5: 1.08 msec per loop
```

- Convert numpy array from `unit8` to `float32`

```bash
# np.float32(img)
python -m timeit "import cvbenchmark as cb; cb.np_unit8_to_float32_constructor_run()"
# 5000 loops, best of 5: 67.1 usec per loop

# img.astype(np.float32)
python -m timeit "import cvbenchmark as cb; cb.np_unit8_to_float32_astype_run()"
# 5000 loops, best of 5: 68.5 usec per loop
```

- Stack a list of np array (non-contiguous) along axis 0.

```bash
# np.array(imgs)
python -m timeit -n 50 "import cvbenchmark as cb; cb.img_list_stack_constructor_run()"
# 50 loops, best of 5: 40 msec per loop

# np.stack(imgs, axis=0)
python -m timeit -n 50 "import cvbenchmark as cb; cb.img_list_stack_stack_run()"
# 50 loops, best of 5: 34.3 msec per loop
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
