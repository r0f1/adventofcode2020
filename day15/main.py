# Van Eck's sequence
# https://oeis.org/A181391
# https://www.youtube.com/watch?v=etMJxB-igrc

# Part 1: Implemented using list

puzzle = "12,1,16,3,11,0"
numbers = [int(n) for n in puzzle.split(",")]

limit = 2020

for _ in range(limit-len(numbers)):
    last = numbers[-1]
    turn = len(numbers)

    ptr = len(numbers)-2
    while ptr >= 0:
        if numbers[ptr] == last:
            numbers.append(turn-(ptr+1))
            break
        ptr -= 1
    else:
        numbers.append(0)

print(numbers[-1])


# Part 2: Reimplemented for efficiency using dict

numbers = [int(n) for n in puzzle.split(",")]
d = {n: (0, t+1) for t, n in enumerate(numbers)}

limit = 30000000

last = numbers[-1]
for turn in range(len(numbers)+1, limit+1):
    if last in d:
        prev_encounter, last_encounter = d[last]
        if prev_encounter == 0:
            last = 0
        else:
            last = last_encounter - prev_encounter
    else:
        last = 0
    
    if last in d:
        prev_encounter, last_encounter = d[last]
        d[last] = (last_encounter, turn)
    else:
        d[last] = (0, turn)

print(last)
