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
# img_array_normalize cv2_div    200 loops, best of 5: 1.81 msec per loop
# img_array_normalize cv2_mult   200 loops, best of 5: 1.68 msec per loop
# img_array_normalize cv2_mult2  200 loops, best of 5: 1.33 msec per loop
# img_array_normalize cv2_mult3  200 loops, best of 5: 1.25 msec per loop
# img_array_normalize cv2_mult4  500 loops, best of 5: 594 usec per loop
# img_array_normalize np         100 loops, best of 5: 2.43 msec per loop
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
./mmbench img_list_stack
# img_list_stack constructor  100 loops, best of 5: 2.12 msec per loop
# img_list_stack stack        200 loops, best of 5: 1.96 msec per loop
```

- Clip bbox

```bash
./mmbench bbox_clip
# bbox_clip clip  50000 loops, best of 5: 4.09 usec per loop
# bbox_clip fast  100000 loops, best of 5: 3.49 usec per loop
# bbox_clip slow  50000 loops, best of 5: 5.71 usec per loop
```

- Permute channel dim before spatial at cpu or gpu.

```bash
$ ./mmbench -n 500 benchmarks/run_permute_at.py
# permute_at cpu  500 loops, best of 5: 1.22 msec per loop
# permute_at gpu  500 loops, best of 5: 478 usec per loop
```

- Pipeline: load -> resize -> crop -> flip -> normalize -> transpose

```bash

## color

# color 400x300 -> x1.41 -> 224x224
./mmbench -n 200 pipeline_color
# pipeline_color opencv          200 loops, best of 5: 4.85 msec per loop
# pipeline_color opencv_fast     200 loops, best of 5: 2.81 msec per loop
# pipeline_color opencv_fastest  200 loops, best of 5: 1.8 msec per loop
# pipeline_color pil             200 loops, best of 5: 2.6 msec per loop
# pipeline_color pil_fast        200 loops, best of 5: 1.85 msec per loop

# color 400x300 -> x0.80 -> 224x224
./mmbench -n 200 pipeline_color_shrink
# pipeline_color_shrink opencv          200 loops, best of 5: 3.26 msec per loop
# pipeline_color_shrink opencv_fast     200 loops, best of 5: 2.13 msec per loop
# pipeline_color_shrink opencv_fastest  200 loops, best of 5: 1.89 msec per loop
# pipeline_color_shrink pil             200 loops, best of 5: 1.81 msec per loop
# pipeline_color_shrink pil_fast        200 loops, best of 5: 1.86 msec per loop

# color 800x600 -> x0.426 -> 224x224
./mmbench -n 200 pipeline_color_shrink_big
# pipeline_color_shrink_big opencv          200 loops, best of 5: 7.22 msec per loop
# pipeline_color_shrink_big opencv_fast     200 loops, best of 5: 3.1 msec per loop
# pipeline_color_shrink_big opencv_fastest  200 loops, best of 5: 2.65 msec per loop
# pipeline_color_shrink_big pil             200 loops, best of 5: 2.7 msec per loop
# pipeline_color_shrink_big pil_fast        200 loops, best of 5: 2.87 msec per loop

# color 133x100 -> x2.56 -> 224x224
./mmbench -n 200 pipeline_color_small
# pipeline_color_small opencv          200 loops, best of 5: 1.91 msec per loop
# pipeline_color_small opencv_fast     200 loops, best of 5: 1.4 msec per loop
# pipeline_color_small opencv_fastest  200 loops, best of 5: 1.14 msec per loop
# pipeline_color_small pil             200 loops, best of 5: 1.23 msec per loop
# pipeline_color_small pil_fast        200 loops, best of 5: 1.18 msec per loop


## gray

# gray 400x300 -> x1.41 -> 224x224
./mmbench -n 200 pipeline_gray
# pipeline_gray opencv          200 loops, best of 5: 1.63 msec per loop
# pipeline_gray opencv_fast     200 loops, best of 5: 1.33 msec per loop
# pipeline_gray opencv_fastest  200 loops, best of 5: 865 usec per loop
# pipeline_gray pil             200 loops, best of 5: 2.31 msec per loop
# pipeline_gray pil_fast        200 loops, best of 5: 1.19 msec per loop

# gray 400x300 -> x0.80 -> 224x224
./mmbench -n 200 pipeline_gray_shrink
# pipeline_gray_shrink opencv          200 loops, best of 5: 1.59 msec per loop
# pipeline_gray_shrink opencv_fast     200 loops, best of 5: 1.28 msec per loop
# pipeline_gray_shrink opencv_fastest  200 loops, best of 5: 898 usec per loop
# pipeline_gray_shrink pil             200 loops, best of 5: 2.3 msec per loop
# pipeline_gray_shrink pil_fast        200 loops, best of 5: 1.22 msec per loop

# gray 133x100 -> x2.56 -> 224x224
./mmbench -n 200 pipeline_gray_small
# pipeline_gray_small opencv          200 loops, best of 5: 445 usec per loop
# pipeline_gray_small opencv_fast     200 loops, best of 5: 434 usec per loop
# pipeline_gray_small opencv_fastest  200 loops, best of 5: 428 usec per loop
# pipeline_gray_small pil             200 loops, best of 5: 942 usec per loop
# pipeline_gray_small pil_fast        200 loops, best of 5: 727 usec per loop


## batch

./mmbench -n 10 pipeline_color_batch
# pipeline_color_batch opencv          10 loops, best of 5: 265 msec per loop
# pipeline_color_batch opencv_fast     10 loops, best of 5: 145 msec per loop
# pipeline_color_batch opencv_fastest  10 loops, best of 5: 88.4 msec per loop
# pipeline_color_batch pil             10 loops, best of 5: 99.8 msec per loop
# pipeline_color_batch pil_fast        10 loops, best of 5: 96 msec per loop

./mmbench -n 10 pipeline_color_shrink_batch
# pipeline_color_shrink_batch opencv          10 loops, best of 5: 187 msec per loop
# pipeline_color_shrink_batch opencv_fast     10 loops, best of 5: 119 msec per loop
# pipeline_color_shrink_batch opencv_fastest  10 loops, best of 5: 100 msec per loop
# pipeline_color_shrink_batch pil             10 loops, best of 5: 90.7 msec per loop
# pipeline_color_shrink_batch pil_fast        10 loops, best of 5: 101 msec per loop

./mmbench -n 10 pipeline_color_small_batch
# pipeline_color_small_batch opencv          10 loops, best of 5: 103 msec per loop
# pipeline_color_small_batch opencv_fast     10 loops, best of 5: 67.1 msec per loop
# pipeline_color_small_batch opencv_fastest  10 loops, best of 5: 46.2 msec per loop
# pipeline_color_small_batch pil             10 loops, best of 5: 52.4 msec per loop
# pipeline_color_small_batch pil_fast        10 loops, best of 5: 49.7 msec per loop


## gpu

./mmbench -n 100 img_array_normalize_at
# img_array_normalize_at cpu  100 loops, best of 5: 2.57 msec per loop
# img_array_normalize_at gpu  100 loops, best of 5: 486 usec per loop
```


## Setup

```bash
conda uninstall -y --force pillow pil jpeg libtiff libjpeg-turbo
pip   uninstall -y         pillow pil jpeg libtiff libjpeg-turbo
conda install -yc conda-forge libjpeg-turbo
CFLAGS="${CFLAGS} -mavx2" pip install --upgrade --no-cache-dir --force-reinstall --no-binary :all: --compile pillow-simd

pip install -U git+git://github.com/lilohuang/PyTurboJPEG.git
```
