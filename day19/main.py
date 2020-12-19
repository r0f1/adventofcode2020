import re

def build_regex(d, rulenum, is_part1):
    if not is_part1:
        if rulenum == "8":
            return build_regex(d, "42", is_part1) + "+"
        elif rulenum == "11":
            a = build_regex(d, "42", is_part1)
            b = build_regex(d, "31", is_part1)
            return "(?:" + "|".join(f"{a}{{{n}}}{b}{{{n}}}" for n in range(1, 100)) + ")"

    rule = d[rulenum]
    if re.fullmatch(r'"."', rule):
        return rule[1]
    else:
        parts = rule.split(" | ")
        res = []
        for part in parts:
            nums = part.split(" ")
            res.append("".join(build_regex(d, n, is_part1) for n in nums))
        return "(?:" + "|".join(res) + ")"

with open("input.txt") as f:
    rules, msgs = [l.rstrip("\n") for l in f.read().split("\n\n")]

d = dict([rule.split(": ") for rule in rules.split("\n")])
msgs = [x.strip() for x in msgs.split("\n")]

for is_part1 in [True, False]:
    z = build_regex(d, "0", is_part1)
    print(sum([bool(re.fullmatch(z, msg)) for msg in msgs]))
