# CV Benchmark

Who is fast, and who is the fastest.

## Results

- Read a `.jpeg` color image as an numpy array.

```bash
./mmbench jpg2np_color
# jpg2np opencv     200 loops, best of 5: 1.51 msec per loop
# jpg2np turbojpeg  500 loops, best of 5: 624 usec per loop
```

- Read a `.jpeg` gray scale image as an numpy array.

```bash
./mmbench jpg2np_gray
# jpg2np_gray opencv     500 loops, best of 5: 658 usec per loop
# jpg2np_gray turbojpeg  500 loops, best of 5: 451 usec per loop
```

- Read a `.jpeg` color image from bytes to an numpy array.

```bash
./mmbench jpgbytes2np_color
# jpgbytes2np_color opencv     200 loops, best of 5: 1.39 msec per loop
# jpgbytes2np_color turbojpeg  500 loops, best of 5: 608 usec per loop
```

- Read a `.jpeg` gray scale image from bytes to an numpy array.

```bash
./mmbench jpgbytes2np_gray
# jpgbytes2np_gray opencv     500 loops, best of 5: 629 usec per loop
# jpgbytes2np_gray turbojpeg  500 loops, best of 5: 438 usec per loop
```

- Image array normalization

```bash
./mmbench img_array_normalize
# img_array_normalize cv2_div   200 loops, best of 5: 1.18 msec per loop
# img_array_normalize cv2_mult  200 loops, best of 5: 1.02 msec per loop
# img_array_normalize np        100 loops, best of 5: 2.09 msec per loop
```

- Convert numpy array from `unit8` to `float32`

```bash
./mmbench np_uint8_to_float32
# np_uint8_to_float32 astype       5000 loops, best of 5: 69 usec per loop
# np_uint8_to_float32 constructor  5000 loops, best of 5: 67.8 usec per loop
```

- Stack a list of np array (non-contiguous) along axis 0.
**This test is unstable. Not sure why, yet**

```bash
./mmbench -n 10 img_list_stack
# img_list_stack constructor  10 loops, best of 5: 46.4 msec per loop
# img_list_stack stack        10 loops, best of 5: 36.6 msec per loop
```

- Clip bbox

```bash
./mmbench bbox_clip
# bbox_clip clip  50000 loops, best of 5: 4.09 usec per loop
# bbox_clip fast  100000 loops, best of 5: 3.49 usec per loop
# bbox_clip slow  50000 loops, best of 5: 5.71 usec per loop
```

- Pipeline: load -> resize -> crop -> flip -> normalize -> transpose

```bash
./mmbench pipeline
# pipeline opencv       200 loops, best of 5: 4.67 msec per loop
# pipeline opencv_fast  200 loops, best of 5: 2.94 msec per loop
# pipeline pil          200 loops, best of 5: 2.44 msec per loop
# pipeline pil_fast     200 loops, best of 5: 1.91 msec per loop
```
