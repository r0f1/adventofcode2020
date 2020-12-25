from collections import namedtuple
from itertools import product

import numpy as np
from imgaug.augmenters.flip import fliplr
from imgaug.augmenters.geometric import Rot90
from scipy.ndimage import generic_filter

OrientedTile = namedtuple("OrientedTile", "idx data")

ndim = 12
with open("input.txt") as f:
    parts = f.read().split("\n\n")

tiles = {}
for p in parts[:-1]:
    p = p.split("\n")
    k = [list(x) for x in p[1:]]
    a = (np.array(k) == "#").astype(np.uint8)
    tiles[int(p[0].split()[1][:-1])] = a

def transform(tile, rot, lr):
    t = Rot90(rot).augment_image(tile)
    if lr:
        t = fliplr(t)
    return t

def get_all_transforms(arr):
    return [transform(arr, r, f) for r, f in product([0,1,2,3], [False, True])]

def edge_has_fit(tiles, tile_idx, edge):
    tile_data = tiles[tile_idx]

    if   edge == 0: e = tile_data[0]
    elif edge == 1: e = tile_data[:,-1]
    elif edge == 2: e = tile_data[-1]
    elif edge == 3: e = tile_data[:,0]

    for idx, tile in tiles.items():
        if idx == tile_idx: continue

        for t in get_all_transforms(tile):
            if np.array_equal(t[0], e):
                return idx
    return None

corners = []
for tile_idx in tiles:
    ns = [edge_has_fit(tiles, tile_idx, i) for i in range(4)]
    if len([e for e in ns if e is not None]) == 2:
        corners.append(tile_idx)
    if len(corners) == 4:
        break
print(int(np.prod(corners)))

# Part 2
def find_neighbor(tiles, tile, direction, seen):
    if direction == "right":
        arr = tile.data[:,-1]
    elif direction == "down":
        arr = tile.data[-1]

    for t_idx, t_data in tiles.items():
        if t_idx == tile.idx: continue
        if t_idx in seen: continue
        
        for data in get_all_transforms(t_data):
            if   direction == "right" and np.array_equal(arr, data[:,0]):
                return OrientedTile(t_idx, data)
            elif direction == "down"  and np.array_equal(arr, data[0]):
                return OrientedTile(t_idx, data)

    raise Exception()

corner_idx = corners[0]
for corner_data in get_all_transforms(tiles[corner_idx]):
    try:
        seen = set()
        display = [[] for _ in range(ndim)]
        display[0].append(OrientedTile(corner_idx, corner_data))
        seen.add(corners[0])

        for idx_row in range(ndim):
            row = display[idx_row]
            while len(row) < ndim:
                n = find_neighbor(tiles, row[-1], "right", seen)
                row.append(n)
                seen.add(n.idx)

            if idx_row < ndim-1:
                n = find_neighbor(tiles, row[0], "down", seen)
                display[idx_row+1].append(n)
                seen.add(n.idx)
    except:
        continue
    break

display2 = np.concatenate([np.concatenate([t.data[1:-1, 1:-1] for t in row], axis=1) for row in display])

nessi = np.array([list("                  # "), 
                  list("#    ##    ##    ###"),
                  list(" #  #  #  #  #  #   ")])
nessi = (nessi == "#").astype(np.uint8)

def f(part):
    part = np.reshape(part, nessi.shape)
    for y, row in enumerate(part):
        for x, pix in enumerate(row):
            if nessi[y][x] == 1 and pix == 0:
                return 0
    return 1

found = max([np.sum(generic_filter(img, f, nessi.shape, mode="constant", cval=0)) for img in get_all_transforms(display2)])
roughness = int(np.count_nonzero(display2) - found*np.sum(nessi))
print(roughness)
