from itertools import combinations

with open("input.txt") as f:
    numbers = [int(x) for x in f]

p = 25
for i in range(len(numbers)-p):
    n = numbers[i+p]
    for a, b in combinations(numbers[i:i+p], 2):
        if a+b == n:
            break
    else:
        print(n)
        break

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        elems = numbers[i:j]
        if sum(elems) == n:
            print(min(elems)+max(elems))
            break
    else:
        continue
    break
