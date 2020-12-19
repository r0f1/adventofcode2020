import numpy as np
from scipy.ndimage import generic_filter

with open("input.txt") as f:
    lines = [list(x.strip()) for x in f]

def f(x):
    if x[len(x) // 2] == 0:
        if np.sum(x) == 3: return 1
        else: return 0
    else:
        if np.sum(x) in (3,4): return 1
        else: return 0

d = 20
for dims in [3,4]:
    a = (np.array(lines) == "#").astype(np.uint8)
    for _ in range(dims-2):
        a = np.reshape(a, (1,)+a.shape)
    arr = np.pad(a, (d-a.shape[0]) // 2)
    kernel = np.ones([3]*dims, dtype=np.uint8)
    for i in range(6):
        arr = generic_filter(arr, f, footprint=kernel, mode="constant", cval=0)
    print(np.sum(arr))
