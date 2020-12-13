import numpy as np
from math import prod

with open("input.txt") as f:
    lines = [x.strip() for x in f]

arrival = int(lines[0])
buses = [(i, int(e)) for i, e in enumerate(lines[1].split(",")) if e.isdigit()]

times = [t for _, t in buses]
b = [e - (arrival % e) for e in times]
print(np.min(b) * times[np.argmin(b)])

def crt(ns, bs):
    # Chinese Remainder Theorem
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    N = prod(ns)
    x = sum(b * (N // n) * pow(N // n, -1, n) for b, n in zip(bs, ns))
    return x % N

offsets = [time-idx for idx, time in buses]
print(crt(times, offsets))
