from parse import findall, search

def parse(b):
    return search('{} bags', b)[0], [*findall('{:d} {} bag', b)]

b = dict(map(parse, open('input.txt')))

def f(c): return any(d == t or f(d) for _, d in b[c])
def g(c): return sum(n * (1 + g(d)) for n, d in b[c])

t = 'shiny gold'
print(sum(map(f, b)), g(t))
