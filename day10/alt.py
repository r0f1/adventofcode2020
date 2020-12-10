import numpy as np

with open("input.txt") as file:
    d = sorted(map(int, file.readlines()))

df = np.array([1] + list(np.diff(d)) + [3])
rle = np.diff([-1] + [i for i, x in enumerate(np.diff(df)) if x != 0] + [len(df)-1])
m = [2**x - sum("000" in bin(y)[2:].zfill(x) for y in range(2**x)) for x in range(max(rle) + 1)]
print((df == 1).sum()*(df == 3).sum())
print(np.prod([m[x-1] for i, x in enumerate(rle) if i % 2 == 0]))
