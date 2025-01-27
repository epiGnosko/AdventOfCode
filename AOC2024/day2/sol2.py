def issafe(x):
    mul = 1
    if x[0] - x[1] < 0:
        mul = -1
    for i in range(len(x)-1):
        if mul*(x[i] - x[i + 1]) > 3 or mul*(x[i] - x[i + 1]) < 1:
            return False
    return True


with open("text2.txt") as f:
    inp = f.readlines()

for i in range(len(inp)):
    inp[i] = inp[i].split(" ")
    for j in range(len(inp[i])):
        inp[i][j] = int(inp[i][j].strip())

safe = 0
for i in inp:
    if issafe(i):
        safe += 1

print(safe)
