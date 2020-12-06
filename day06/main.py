from collections import Counter

with open("input.txt") as f:
    lines = [x.strip() for x in f]

grps = []
g = []
for line in lines:
    if len(line) == 0:
        grps.append(g)
        g = []
    else:
        g.append(line)
grps.append(g)
    
print(sum([len(Counter("".join(g))) for g in grps]))
print(sum([len([v for v in Counter("".join(g)).values() if v == len(g)]) for g in grps]))
