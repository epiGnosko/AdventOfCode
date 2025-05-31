def count_neigh(state, x, y):
    count = 0
    for i in (-1,0,1):
        if x == 0 and i == -1:
            continue
        if x == len(state) - 1 and i == 1:
            continue
        for j in (-1,0,1):
            if y == 0 and j == -1:
                continue
            if y == len(state[x]) - 1 and j == 1:
                continue
            if state[x+i][y+j] == "#":
                count += 1
    if state[x][y] == "#":
        count -= 1
    return count

def next(state):
    newstate = [row.copy() for row in state]
    for i in range(len(state)):
        for j in range(len(state[i])):
            lighted_neighbours = count_neigh(state, i, j)
            if state[i][j] == "#" and lighted_neighbours != 2 and lighted_neighbours != 3:
                newstate[i][j] = "."
            elif state[i][j] == "." and lighted_neighbours == 3:
                newstate[i][j] = "#"
    return newstate


with open("input.txt") as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()

    state = []
    for line in data:
        row = []
        for char in line:
            row.append(char)
        state.append(row.copy())

for i in range(100):
    print()
    print("Step",i+1)
    for j in state:
        for k in j:
            print(k, end="")
        print()
    state = next(state)

count = 0
for i in state:
    for j in i:
        if j == "#":
            count += 1

print(count)
