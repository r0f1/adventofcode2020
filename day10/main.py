import numpy as np
from more_itertools import run_length

with open("input.txt") as f:
    numbers = sorted([int(x) for x in f])

k = np.diff(numbers)
print((1+(k == 1).sum()) * (1+(k == 3).sum()))

cands = [e for i, e in run_length.encode(np.diff([0]+numbers)) if i == 1 and e > 1]
# Tribonacci numbers - http://oeis.org/wiki/Tribonacci_numbers 
# 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, ...
combinations = {2: 2, 3: 4, 4: 7}
print(np.prod([combinations[e] for e in cands]))
