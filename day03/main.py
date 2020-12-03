import math

with open("input.txt") as f:
    lines = [x.strip() for x in f]

width = len(lines[0])
result = []
for dx, dy in [(3,1), (1,1), (5,1), (7,1), (1,2)]:
    ctr = 0
    for i in range(len(lines) // dy):
        y = i * dy
        x = (i * dx) % width
        if lines[y][x] == "#":
            ctr += 1
    result.append(ctr)

print(result[0])
print(math.prod(result))
