def solve(numbers, until):
    memory = {n: i+1 for i, n in enumerate(numbers[:-1])}
    for i in range(len(numbers), until):
        numbers.append(i - memory.get(numbers[-1], i))
        memory[numbers[-2]] = i
    return numbers[-1]

numbers = [int(n) for n in "12,1,16,3,11,0".split(",")]
print(solve(numbers, 2020))
print(solve(numbers, 30000000))
