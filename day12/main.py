from parse import search

with open("input.txt") as f:
    code = [search("{}{:d}", x).fixed for x in f]

posx = 0
posy = 0
dirs = ["E", "S", "W", "N"]
ptr = 0

for d, n in code:
    if   d == "N": posy += n
    elif d == "S": posy -= n
    elif d == "E": posx += n
    elif d == "W": posx -= n
    elif d == "L": ptr = (ptr - n // 90) % len(dirs)
    elif d == "R": ptr = (ptr + n // 90) % len(dirs)
    elif d == "F":
        if   dirs[ptr] == "N": posy += n
        elif dirs[ptr] == "S": posy -= n
        elif dirs[ptr] == "E": posx += n
        elif dirs[ptr] == "W": posx -= n
    
print(abs(posx)+abs(posy))

wpx = 10
wpy = 1
posx = 0
posy = 0

for d, n in code:
    if   d == "N": wpy += n
    elif d == "S": wpy -= n
    elif d == "E": wpx += n
    elif d == "W": wpx -= n
    elif d in ("R", "L") and n == 180:
        wpx, wpy = -wpx, -wpy
    elif d == "R":
        if n == 90:    wpx, wpy =  wpy, -wpx
        elif n == 270: wpx, wpy = -wpy,  wpx
    elif d == "L":
        if n == 90:    wpx, wpy = -wpy,  wpx
        elif n == 270: wpx, wpy =  wpy, -wpx
    elif d == "F":
        posx += n * wpx
        posy += n * wpy
    
print(abs(posx)+abs(posy))
