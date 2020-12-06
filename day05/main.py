g = lambda s: int("".join([str(int(n == 'B' or n == 'R')) for n in s]), 2)

with open("input.txt") as f:
    seats = set(g(x.strip()) for x in f)

print(max(seats))
for i in range(min(seats), max(seats)):
    if i not in seats:
        print(i)
