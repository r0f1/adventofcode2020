import numpy as np
from more_itertools import run_length

with open("input.txt") as f:
    numbers = sorted([int(x) for x in f])

k = np.diff(numbers)
print((1+len(k[k == 1])) * (1+len(k[k == 3])))

# 1 --> ignore
# 2 --> 1, 0 (2)
# 3 --> 1 1, 1 0, 0 1, 0 0 (4)
# 4 --> 1 1 1, 1 0 0, 0 1 0, 0 0 1, 1 1 0, 1 0 1, 0 1 1 (7)
cands = [e for i, e in run_length.encode(np.diff([0]+numbers)) if i == 1 and e > 1]
t = {2: 2, 3: 4, 4: 7}
transformed = [t[e] for e in cands]
print(np.prod(transformed))
