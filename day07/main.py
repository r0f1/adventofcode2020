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

def check(color, k):
    for c in d[color]:
        k.add(c)
        check(c, k)
    return k

print(len(check("shiny gold", set())))

def count(color):
    return 1 + sum(n * count(c) for c, n in d2[color] if n > 0)

print(count("shiny gold")-1)
    