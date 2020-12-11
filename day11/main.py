from itertools import product, cycle

import numpy as np
from scipy.ndimage import convolve

def check(grid, cols, rows):
    for c, r in zip(cols, rows):
        k = grid[c, r]
        if k in (1,2):
            return k-1
    return 0

def get_neightbors(grid, orig_grid, is_part1):
    if is_part1:
        kernel = np.ones((3,3), dtype=np.int8)
        kernel[1,1] = 0
        empty = convolve(orig_grid, kernel, mode="constant", cval=0)
        return convolve(grid, kernel, mode="constant", cval=0) - empty
    else:
        res = np.zeros_like(grid)
        col, row = grid.shape
        for r, c in product(range(row), range(col)):
            if grid[c,r] == 0:
                continue
            else:
                n  = check(grid, cycle([c]),         reversed(range(r)))  # left
                n += check(grid, cycle([c]),         range(r+1, row))     # right
                n += check(grid, reversed(range(c)), cycle([r]))          # up
                n += check(grid, range(c+1, col),    cycle([r]))          # down

                n += check(grid, reversed(range(c)), reversed(range(r))) # diag left up
                n += check(grid, range(c+1, col),    reversed(range(r))) # diag left down
                n += check(grid, reversed(range(c)), range(r+1, row))    # diag right up
                n += check(grid, range(c+1, col),    range(r+1, row))    # diag right down

                res[c,r] = n

        return res

with open("input.txt") as f:
    rows = []
    for x in f:
        rows.append([c == "L" for c in x.strip()])

for is_part1 in [True, False]:

    if is_part1:
        cutoff = 4
    else:
        cutoff = 5

    grid = np.array(rows).astype(np.int8)
    seats = grid.copy()
    occ = (grid == 2).sum()

    while True:
        prev_occ = occ
        n = get_neightbors(grid, seats, is_part1)
        u = (n == 0).astype(int) - (n >= cutoff).astype(int)
        u[grid == 0] = 0
        grid = np.clip(grid + u, 0, 2)
        grid[grid == 0] = seats[grid == 0]
        occ = (grid == 2).sum()
        if occ == prev_occ:
            break

    print(occ)
