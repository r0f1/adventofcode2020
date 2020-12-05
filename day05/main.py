def g(s):
    r = int("".join([str(int(n == 'B')) for n in s[:7]]), 2)
    c = int("".join([str(int(n == 'R')) for n in s[7:]]), 2)
    return r*8+c

with open("input.txt") as f:
    seats = set(g(x.strip()) for x in f)

print(max(seats))
for i in range(min(seats), max(seats)):
    if i not in seats:
        print(i)
