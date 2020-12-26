
class Node:
    def __init__(self, n, pred, succ):
        self.n = n
        self.pred = pred
        self.succ = succ

def to_linked_list(l):
    prev = Node(l[0], None, None)
    f = prev
    for e in l[1:]:
        n = Node(e, prev, None)
        prev.succ = n
        prev = n
    n.succ = f
    f.pred = n
    return f

def to_dict(curr):
    d = {}
    n = curr.n
    d[n] = curr
    while True:
        curr = curr.succ
        if curr.n == n: break
        d[curr.n] = curr
    return d

def to_list(curr):
    first = curr.n
    res = [first]
    while True:
        curr = curr.succ
        if curr.n == first: break
        res.append(curr.n)
    return res

def make_move(curr, d, l):
    act = curr
    f1 = curr.succ
    f2 = f1.succ
    f3 = f2.succ

    curr.succ = f3.succ
    f3.pred = curr

    n = curr.n
    while True:
        n -= 1
        if n == 0:
            n = l
        if n not in [f1.n, f2.n, f3.n]:
            break

    curr = d[n]

    k = curr.succ
    curr.succ = f1
    f1.pred = curr
    f3.succ = k
    k.pred = f3
    return act.succ

for is_part1 in [True, False]:
    n = [int(i) for i in "476138259"]

    if is_part1:
        n_moves = 100
    else:
        n += list(range(10, 1_000_001))
        n_moves = 10_000_000

    l = len(n)
    n = to_linked_list(n)
    d = to_dict(n)

    for move in range(n_moves):
        n = make_move(n, d, l)

    k = to_list(d[1])
    if is_part1:
        print("".join(str(c) for c in k[1:]))
    else:
        print(k[1]*k[2])
