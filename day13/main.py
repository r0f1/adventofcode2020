import numpy as np
from math import prod

with open("input.txt") as f:
    lines = [x.strip() for x in f]

arrival = int(lines[0])
buses = [(i, int(e)) for i, e in enumerate(lines[1].split(",")) if e.isdigit()]

offsets, times = zip(*buses)
b = [e - (arrival % e) for e in times]
print(np.min(b) * times[np.argmin(b)])

def chinese_remainder(ns, rems):
    p = prod(ns)
    x = sum(r * (p // n) * pow(p // n, -1, n) for r, n in zip(rems, ns))
    return x % p

rems = [time-offset for offset, time in buses]
print(chinese_remainder(times, rems))
