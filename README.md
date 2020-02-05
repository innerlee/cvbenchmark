# CV Benchmark

Who is fast, and who is the fastest.

## Results

- Read a `.jpeg` image as an numpy array.

```bash
./mmbench jpg2np
# jpg2np opencv     200 loops, best of 5: 1.54 msec per loop
# jpg2np turbojpeg  500 loops, best of 5: 663 usec per loop
```

- Image array normalization

```bash
./mmbench img_array_normalize
# img_array_normalize cv2_div   200 loops, best of 5: 1.31 msec per loop
# img_array_normalize cv2_mult  200 loops, best of 5: 1.19 msec per loop
# img_array_normalize np        100 loops, best of 5: 2.15 msec per loop
```

- Convert numpy array from `unit8` to `float32`

```bash
./mmbench np_uint8_to_float32
# np_uint8_to_float32 astype       5000 loops, best of 5: 68.3 usec per loop
# np_uint8_to_float32 constructor  5000 loops, best of 5: 68.8 usec per loop
```

- Stack a list of np array (non-contiguous) along axis 0.
**This test is unstable. Not sure why, yet**

```bash
./mmbench -n 10 img_list_stack
# img_list_stack constructor  10 loops, best of 5: 56.2 msec per loop
# img_list_stack stack        10 loops, best of 5: 54.8 msec per loop
```

- Clip bbox

```bash
./mmbench bbox_clip
# bbox_clip clip  20000 loops, best of 5: 10.1 usec per loop
# bbox_clip fast  50000 loops, best of 5: 9.15 usec per loop
# bbox_clip slow  20000 loops, best of 5: 11.6 usec per loop
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
