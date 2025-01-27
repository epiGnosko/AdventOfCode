def parse(i, j):
    dir1 = [-1, 0, 1]
    dir2 = [-1, 0, 1]
    out = "MAS"

    count = 0
    for m in dir1:
        for n in dir2:
            for o in range(3):
                found = True
                rowpar = i + (o + 1) * m
                colpar = j + (o + 1) * n
                if rowpar not in range(len(inp)) or colpar not in range(len(inp[0])):
                    found = False
                    break
                if inp[rowpar][colpar] != out[o]:
                    found = False
                    break
            if found:
                count += 1

    return count


with open("text4.txt") as f:
    inp = f.readlines()

netcount = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == "X":
            netcount += parse(i, j)

print(netcount)
