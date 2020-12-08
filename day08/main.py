
code = []
with open("input.txt") as f:
    for x in f:
        i, n = x.strip().split()
        code.append((i, int(n)))

def execute(instrs):
    visited = set()
    pc = 0
    acc = 0
    while True:
        if pc == len(code):
            return acc, "OK"
        if pc in visited:
            return acc, "ERROR"
        visited.add(pc)
        c, n = instrs[pc]
        if   c == "acc": acc += n
        elif c == "jmp": pc += n-1
        elif c == "noop": pass
        pc += 1

print(execute(code)[0])

for i in range(len(code)):
    c, n = code[i]
    if c in ("jmp", "noop"):
        code2 = code[:]
        if c == "jmp": code2[i] = ("noop", n)
        else: code2[i] = ("jmp", n)
        
        res, exit_code = execute(code2)
        if exit_code == "OK":
            print(res)
            break
