with open("input.txt") as f:
    grps = f.read().split('\n\n')

print(sum(len(set.union(*[set(i) for i in a.split()])) for a in grps))
print(sum(len(set.intersection(*[set(i) for i in a.split()])) for a in grps))
