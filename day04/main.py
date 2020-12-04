import re

with open("input.txt") as f:
    lines = [x.strip() for x in f]

expected = set("byr iyr eyr hgt hcl ecl pid".split())
passports = []
ctr = 0
while ctr < len(lines):
    k = ""
    while len(lines[ctr]) > 0:
        k += " " + lines[ctr]
        ctr += 1
        if ctr == len(lines):
            break
    passports.append(k)
    ctr += 1

valids = 0
valids2 = 0
for p in passports:
    chunks = p.split()
    actual = set([c.split(":")[0] for c in chunks])
    if len(expected - actual) == 0:
        valids += 1
        d = dict([c.split(":") for c in chunks])
        c1 = len(d["byr"]) == 4 and 1920 <= int(d["byr"]) <= 2002
        c2 = len(d["iyr"]) == 4 and 2010 <= int(d["iyr"]) <= 2020
        c3 = len(d["eyr"]) == 4 and 2020 <= int(d["eyr"]) <= 2030
        c4 = (re.match("^\d\d\dcm$", d["hgt"]) is not None and 150 <= int(d["hgt"][:-2]) <= 193) or (re.match("^\d\din$", d["hgt"]) is not None and 59 <= int(d["hgt"][:-2]) <= 76)
        c5 = re.match("^#[a-f0-9]{6}$", d["hcl"]) is not None
        c6 = d["ecl"] in ("amb blu brn gry grn hzl oth".split())
        c7 = re.match("^\d{9}$", d["pid"]) is not None
        if all([c1, c2, c3, c4, c5, c6, c7]):
            valids2 += 1

print(valids)
print(valids2)
