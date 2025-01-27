def parse(string, index):
    parser = index
    if string[parser] != '(':
        return 0
    parser += 1
    int1 = 0
    while string[parser] != ',':
        if not string[parser].isdigit():
            return 0
        int1 *= 10
        int1 += int(string[parser])
        parser += 1
    parser += 1
    int2 = 0
    while string[parser] != ')':
        if not string[parser].isdigit():
            return 0
        int2 *= 10
        int2 += int(string[parser])
        parser += 1
    return int1 * int2


with open("text3.txt") as f:
    inp = f.readlines()

accumulator = 0
active = True
for i in inp:
    for j in range(len(i)-3):
        if i[j:j+3] == "mul" and active:
            accumulator += parse(i, j+3)
        elif i[j:j+7] == "don't()":
            active = False
        elif i[j:j+4] == "do()":
            active = True

print(accumulator)
