from collections import Counter

with open("input.txt") as f:
    grps = [x.strip().split() for x in f.read().split("\n\n")]
    
print(sum([len(Counter("".join(g))) for g in grps]))
print(sum([len([v for v in Counter("".join(g)).values() if v == len(g)]) for g in grps]))
