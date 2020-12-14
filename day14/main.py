from itertools import product
from parse import search

def possible_addrs(mask, addr):
    mask2 = "".join(v if m == "0" else m for m, v in zip(mask, f"{addr:036b}"))
    res = []
    for t in product("01", repeat=mask2.count("X")):
        it = iter(t)
        res.append(int("".join(next(it) if c == "X" else c for c in mask2), 2))
    return res

with open("input.txt") as f:
    lines = [x.strip() for x in f]

for is_part1 in [True, False]:
    mask = ""
    mem = {}
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            arg1, arg2 = search("mem[{:d}] = {:d}", line).fixed
            if is_part1:
                mem[arg1] = int("".join(v if m == "X" else m for m, v in zip(mask, f"{arg2:036b}")), 2)
            else:
                for addr in possible_addrs(mask, arg1):
                    mem[addr] = arg2

    print(sum(mem.values()))
