from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip() for x in f]

d = defaultdict(list)
d2 = defaultdict(list)

for line in lines:
    color1 = " ".join(line.split()[:2])
    chunks = line.split("contain ")[1].split(", ")
    for c in chunks:
        color2 = " ".join(c.split()[1:3])
        d[color2].append(color1)
        q = c.split()[0]
        if q == "no":
            d2[color1].append((color2, 0))
        else:
            d2[color1].append((color2, int(q)))

s = d["shiny gold"]
res = set()
while s:
    c = s.pop()
    if c in res:
        continue
    res.add(c)
    s.extend(d[c])
print(len(res))

def count(color):
    bags = d2[color]
    res = 0
    for c, n in bags:
        if n > 0:
            res += n * count(c)
    return 1 + res

print(count("shiny gold")-1)
    