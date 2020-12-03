from pathlib import Path
import numpy as np

lines = Path("input.txt").read_text().strip().split("\n")
width = len(lines[0])
result = []
for dx, dy in [(3,1), (1,1), (5,1), (7,1), (1,2)]:
    ctr = 0
    x = 0
    for line in lines[::dy]:
        ctr += line[x] == '#'
        x = (x + dx) % width
    result.append(ctr)

print(result[0])
print(np.prod(result))
