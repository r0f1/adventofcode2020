with open("input.txt") as f:
    public_key_card, public_key_door = [int(x.strip()) for x in f]

def calc_loop_size(public_key):
    subject_number = 7
    n = 1
    i = 0
    while True:
        n = (n * subject_number) % 20201227
        if n == public_key:
            return i+1
        i += 1

def calc_encryption_key(subject_number, loop_size):
    n = 1
    for i in range(loop_size):
        n = (n * subject_number) % 20201227
    return n

loop_size = calc_loop_size(public_key_card)
enc_key = calc_encryption_key(public_key_door, loop_size)
print(enc_key)
