from collections import namedtuple
from itertools import product, permutations

import numpy as np
from imgaug.augmenters.flip import fliplr, flipud
from imgaug.augmenters.geometric import Rot90
from tqdm import tqdm

Tile = namedtuple("Tile", "idx ns ts e")

with open("input2.txt") as f:
    parts = f.read().split("\n\n")

tiles = {}
for p in parts[:-1]:
    p = p.split("\n")
    k = [list(x) for x in p[1:]]
    a = (np.array(k) == "#").astype(np.uint8)
    tiles[int(p[0].split()[1][:-1])] = a

def transform(tile, rot, lr, ud):
    t = Rot90(rot).augment_image(tile)
    if lr:
        t = fliplr(t)
    if ud:
        t = flipud(t)
    return t

def edge_has_fit(tiles, tile_idx, edge):
    k = tiles[tile_idx]
    
    if   edge == 0: e = k[0]
    elif edge == 1: e = k[:,-1]
    elif edge == 2: e = k[-1]
    elif edge == 3: e = k[:,0]

    for idx, tile in tiles.items():
        if idx == tile_idx: continue

        for trans in product([0,1,2,3], [False, True], [False, True]):
            t = transform(tile, *trans)
            for f in [t[0], t[:,-1], t[-1], t[:,0]]:
                if np.array_equal(f, e):
                    return idx, trans
    return None, None

res = []
# for idx in tqdm(tiles.keys()):
for idx in tiles.keys():
    ns, ts = zip(*[edge_has_fit(tiles, idx, i) for i in range(4)])
    tile = Tile(idx, ns, ts, len([e for e in ns if e is not None]))
    res.append(tile)

# print(int(np.prod(corners)))

corners = [t for t in res if t.e == 2]
edges   = [t for t in res if t.e == 3]
middles = [t for t in res if t.e == 4]

print([(t.idx, t.ns) for t in corners])
print([(t.idx, t.ns) for t in edges])
print([(t.idx, t.ns) for t in middles])
print("\n\n")

nrows = 3
ncols = 3

def rotate(l, n):
    return list(l[n:] + l[:n])

def flip_lr(l):
    return [l[0], l[3], l[2], l[1]]

def flip_ud(l):
    return [l[2], l[1], l[0], l[3]]

def find_and_pop(elems, n_idx):
    res = None
    del_idx = None
    for i, t in enumerate(elems):
        if t.idx == n_idx:
            res = t
            del_idx = i
            break
    else:
        raise RuntimeError(f"{t.idx} was not found in {elems}.")

    del elems[del_idx]
    return res

def match(ns, exp):
    assert len(ns) == len(exp)

    for n, e in zip(ns, exp):
        if e is None:
            if n is not None:
                return False
        else:
            if e == 0:
                continue
            else:
                if n != e:
                    return False
    return True

def place(tile, exp):
    if tile.idx == 1171:
        print("orig")
        print(tile.ns)

    n = tile.ns
    t = tile.ts
    for trans in product([0,1,2,3], [False, True], [False, True]):
        n = rotate(n, trans[0])
        t = rotate(t, trans[0])
        if trans[1]:
            n = flip_lr(n)
            t = flip_lr(t)
        if trans[2]:
            n = flip_ud(n)
            t = flip_ud(t)

        if tile.idx == 1171:
            print(trans[0], "lr?", trans[1], "ud?", trans[2], end=" ")
            print(n, exp)
        if match(n, exp):
            return Tile(tile.idx, n, t, tile.e)
    
    raise RuntimeError(tile)

def print_short(l):
    print([(t.idx, t.ns) for t in l])

layout = []

for idx_row in range(nrows):
    if idx_row == 0:
        tile = corners.pop()
        tile = place(tile, [None, 0, 0, None])
        row = [tile]
    elif idx_row == nrows-1:
        tile = find_and_pop(corners, layout[idx_row-1][0].ns[2])
        upper = layout[idx_row-1][0].idx
        tile = place(tile, [upper, 0, None, None])
        row = [tile]
    else:
        row = [find_and_pop(edges, layout[idx_row-1][0])]

    for idx_col in range(1, ncols):
        prev_tile = row[-1]
        n_idx = prev_tile.ns[1]
        
        print_short(row)
        print(idx_col, n_idx)

        if idx_row in (0, nrows-1):
            if idx_col == ncols-1:
                elems = corners
            else:
                elems = edges
        else:
            if idx_col == ncols-1:
                elems = edges
            else:
                elem = middles

        t = find_and_pop(elems, n_idx)

        if idx_row == 0:
            upper = None
        else:
            upper = layout[idx_row-1][0].idx

        left = prev_tile.idx

        if idx_col == ncols-1:
            if idx_row == 0:
                row.append(place(t, [None, None, 0, left]))

            elif idx_row == nrows-1:
                row.append(place(t, [0, None, None, left]))

            else:
                row.append(place(t, [upper, None, 0, left]))
        else:
            row.append(place(t, [upper, 0, 0, left]))

    layout.append(row)

print(layout)
