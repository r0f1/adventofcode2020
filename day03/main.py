
def slope(dx, dy):
    with open("input.txt") as f:
        lines = [x.strip() for x in f]

    width = len(lines[0])
    x = 0
    y = 0
    ctr = 0
    while y < len(lines):
        if lines[y][x] == '#':
            ctr += 1
        x += dx
        y += dy
        x %= width

    return ctr

print(slope(3,1))
print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))
