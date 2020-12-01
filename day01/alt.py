import itertools
import numpy as np

with open("input.txt") as f:
    ns = [int(x.strip()) for x in f]

print([np.product(n) for n in itertools.combinations(ns, 2) if sum(n) == 2020][0])
print([np.product(n) for n in itertools.combinations(ns, 3) if sum(n) == 2020][0])

####

s = set(ns)
print([a * (2020 - a) for a in s if 2020 - a in s][0])
print([a * b * (2020 - a - b) for a in s for b in s if 2020 - a - b in s][0])

