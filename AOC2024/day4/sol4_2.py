def parse(i, j):
    if inp[i-1][j-1] in "MS" and inp[i+1][j+1] in "MS" and inp[i-1][j-1] != inp[i+1][j+1] and inp[i+1][j-1] in "MS" and inp[i-1][j+1] in "MS" and inp[i+1][j-1] != inp[i-1][j+1]:
        return 1
    return 0


with open("text4.txt") as f:
    inp = f.readlines()

netcount = 0
for i in range(1, len(inp)-1):
    for j in range(1, len(inp[i])-1):
        if inp[i][j] == "A":
            netcount += parse(i, j)

print(netcount)
