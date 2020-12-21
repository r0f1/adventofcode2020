from itertools import product, permutations

import numpy as np
from imgaug.augmenters.flip import fliplr, flipud
from imgaug.augmenters.geometric import Rot90
from tqdm import tqdm

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
                    return idx
    return None

res = []
# for idx in tqdm(tiles.keys()):
for idx in tiles.keys():
    k = [edge_has_fit(tiles, idx, i) for i in range(4)]
    res.append((idx, k, len([e for e in k if e is not None])))

# print(int(np.prod(corners)))

corners = [(idx, n) for idx, n, e in res if e == 2]
edges   = [(idx, n) for idx, n, e in res if e == 3]

print(corners)
print(edges)

# for (idx_tl, n_tl), (idx_tr, n_tl), (idx_bl, n_bl), (idx_br, n_bl) in permutations(corners):
#     print(idx_tl)
    

