import numpy as np

with open("input.txt") as f:
    lines = [x.strip() for x in f]

sep1 = "your ticket:"
sep2 = "nearby tickets:"

part1 = lines[:lines.index(sep1)-1]
part2 = [int(n) for n in lines[lines.index(sep1)+1].split(",")]
part3 = lines[lines.index(sep2)+1:]

alloweds = []
for line in part1:
    a = set()
    ranges = line.split(": ")[1]
    for r in ranges.split(" or "):
        bounds = r.split("-")
        lb, ub = int(bounds[0]), int(bounds[1])
        for i in range(lb, ub+1):
            a.add(i)
    alloweds.append(a)

score = []
c = len(part1)
poss_mat = np.ones((c,c), dtype=np.uint8)

for line in part3:
    okay = True
    numbers = [int(n) for n in line.split(",")]
    for n in numbers:
        if not any(n in a for a in alloweds):
            score.append(n)
            okay = False
    if okay:
        for field_idx, n in enumerate(numbers):
            for j, a in enumerate(alloweds):
                if n not in a:
                    poss_mat[field_idx][j] = 0

print(sum(score))

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

res = 1
for j, row in enumerate(poss_mat):
    if np.argmax(row) < 6:
        res *= part2[j]

print(res)
