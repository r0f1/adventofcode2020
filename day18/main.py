from more_itertools import chunked
from math import prod

with open("input.txt") as f:
    lines = [x.strip() for x in f]

def analyse(s):
    if "(" not in s:
        return calc(s)

    res = {}
    stack = []

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            res[stack.pop()] = i

    a, b = next(iter(res.items()))
    e = analyse(s[a+1: b])
    return analyse(f"{s[:a]}{e}{s[b+1:]}")

def calc1(t):
    s = t.split()
    res = int(s[0])
    for o, n in chunked(s[1:], 2):
        if o == "+":
            res += int(n)
        elif o == "*":
            res *= int(n)
    return res

def calc2(t):
    k = t.split("*")
    return prod(calc1(e) for e in k)

calc = calc1
print(sum(analyse(line) for line in lines))
calc = calc2
print(sum(analyse(line) for line in lines))
