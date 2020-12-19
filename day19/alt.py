from lark import Lark, LarkError

def solve(rules, is_part1):
    if not is_part1:
        rules = rules.replace('8: 42', '8: 42 | 42 8')
        rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
    rules = rules.translate(str.maketrans('0123456789', 'abcdefghij'))
    parser = Lark(rules, start='a')

    total = 0
    for line in lines.splitlines():
        try:
            parser.parse(line)
            total += 1
        except LarkError:
            pass

    return total

with open("input.txt") as f:
    rules, lines = [l.rstrip("\n") for l in f.read().split("\n\n")]

for is_part1 in [True, False]:
    print(solve(rules, is_part1))
