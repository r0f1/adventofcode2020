
# for is_part1 in [True, False]:
for is_part1 in [True, False]:
    # n = [int(i) for i in "476138259"]
    n = [int(i) for i in "389125467"]

    if not is_part1:
        n += list(range(10, 1_000_001))

    if is_part1: 
        n_moves = 100
    else:
        n_moves = 10_000_000

    l = len(n)
    idx = 0
    for move in range(n_moves):
        if move % 100 == 0:
            print(move, end=" ", flush=True)

        curr = n[idx]
        i = (idx + 1) % l
        sel = []
        for _ in range(3):
            sel.append(n[i])
            i = (i + 1) % l

        for e in sel:
            n.remove(e)

        dest = curr
        while True:
            dest -= 1
            if dest == 0:
                dest = l
            if dest not in sel:
                break
        
        pos = n.index(dest) + 1
        n = n[:pos] + sel + n[pos:]
        idx = (n.index(curr) + 1) % l

    print()
    oneidx = n.index(1)
    if is_part1:
        print("".join([str(c) for c in n[oneidx+1:]+n[:oneidx]]))
    else:
        print(n[oneidx+1]*n[oneidx+2])
