with open("test.txt") as f:
    input = f.readline()
    
current_house = [[0,0],[0,0]]
visited = [[0,0]]

for i in range(len(input)):
    if input[i] == "^":
        current_house[i%2][1] += 1
    elif input[i] == "v":
        current_house[i%2][1] -= 1
    elif input[i] == ">":
        current_house[i%2][0] += 1
    elif input[i] == "<":
        current_house[i%2][0] -= 1
    add = current_house[i%2]
    
    print(add)
    if add not in visited:
        visited.append(add.copy())

print(len(visited))

