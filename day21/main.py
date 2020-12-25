from collections import defaultdict

import numpy as np
from more_itertools import flatten

with open("input.txt") as f:
    lines = [x.strip() for x in f]

foods     = [x.split(" (contains ")[0].split() for x in lines]
allergens = [x.split(" (contains ")[1][:-1].split(", ") for x in lines]
recipe    = list(zip(foods, allergens))

poss_allergens = sorted(set(list(flatten(allergens))))

poss = []
for _, pa in enumerate(poss_allergens):
    k = []
    for fs, allergs in recipe:
        if pa in allergs:
            k.append(set(fs))
    poss.append(k)

reduced = [set.intersection(*ps) for ps in poss]
remaining_foods = sorted(set(flatten(reduced)))
count = len([f for f in flatten(foods) if f not in remaining_foods])
print(count)
poss_mat = np.array([[1 if r in red else 0 for r in remaining_foods] for red in reduced])

change = True
seen = set()
while change:
    change = False
    for i, row in enumerate(poss_mat):
        if sum(row) == 1 and i not in seen:
            seen.add(i)
            change = True
            col = np.argmax(row)
            poss_mat[:, col] = 0
            poss_mat[i, col] = 1

print(",".join(remaining_foods[np.argmax(poss_mat[i])] for i in range(len(remaining_foods))))
