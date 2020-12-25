
with open("input.txt") as f:
    chunks = f.read().split("\n\n")

orig_p1 = list(map(int, chunks[0].strip().split("\n")[1:]))
orig_p2 = list(map(int, chunks[1].strip().split("\n")[1:]))

p1 = orig_p1.copy()
p2 = orig_p2.copy()

while len(p1) > 0 and len(p2) > 0:
    a, b = p1.pop(0), p2.pop(0)
    if a > b: 
        p1 += [a,b]
    else:
        p2 += [b,a]

if len(p1) > 0:
    winner = p1
else:
    winner = p2

print(sum(e*(len(winner)-i) for i, e in enumerate(winner)))

# Part 2
def play_game(p1, p2):
    seen1, seen2 = set(), set()

    while len(p1) > 0 and len(p2) > 0:
        s1 = ",".join([str(c) for c in p1])
        s2 = ",".join([str(c) for c in p2])
        if s1 in seen1 or s2 in seen2:
            return "p1", p1
        seen1.add(s1)
        seen2.add(s2)

        a, b = p1.pop(0), p2.pop(0)
        if a <= len(p1) and b <= len(p2):
            winner, _ = play_game(p1.copy()[:a], p2.copy()[:b])
        else:
            if a > b:
                winner = "p1"
            else:
                winner = "p2"
        
        if winner == "p1":
            p1 += [a,b]
        else:
            p2 += [b,a]

    if len(p1) > 0:
        return "p1", p1
    else:
        return "p2", p2
    
_, w = play_game(orig_p1.copy(), orig_p2.copy())
print(sum(e*(len(w)-i) for i, e in enumerate(w)))
