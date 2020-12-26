from collections import defaultdict

def parse(s):
    i = 0
    res = []
    while s:
        if   s[0]   == "w":  res.append((-1,0)); s = s[1:]
        elif s[0]   == "e":  res.append((1,0));  s = s[1:]
        elif s[0:2] == "se": res.append((1,-1)); s = s[2:]
        elif s[0:2] == "sw": res.append((0,-1)); s = s[2:]
        elif s[0:2] == "ne": res.append((0,1));  s = s[2:]
        elif s[0:2] == "nw": res.append((-1,1)); s = s[2:]
    return res

with open("input.txt") as f:
    lines = [parse(x.strip()) for x in f]

d = defaultdict(int)

for line in lines:
    xs, ys = zip(*line)
    coords = sum(ys), sum(xs)
    d[coords] = 1 - d[coords]
    
print(sum(d.values()))

def apply(n, ns):
    if n == 0:
        if sum(ns) == 2:
            return 1
    else:
        if sum(ns) == 0 or sum(ns) > 2:
            return 0
    return n

dirs = [(1,-1),(0,-1),(-1,1),(0,1),(1,0),(-1,0)]
for _ in range(100):
    d2 = d.copy()
    for row in range(-100,100):
        for col in range(-100,100):
            coords = (row,col)
            d2[coords] = apply(d[coords], [d[k] for k in [(y+row, x+col) for x, y in dirs]])
    d = d2

print(sum(d.values()))
