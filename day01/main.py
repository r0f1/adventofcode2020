with open("input.txt") as f:
    l = [int(x.strip()) for x in f]

# Part 1
for i, n1 in enumerate(l):
    for n2 in l[i+1:]:
        if n1 + n2 == 2020:
            print(n1 * n2)
            break

# Part 2
for i, n1 in enumerate(l):
    for j, n2 in enumerate(l[i+1:]):
        for n3 in l[i+j+1:]:
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
                break

# Output:
# 485739
# 161109702