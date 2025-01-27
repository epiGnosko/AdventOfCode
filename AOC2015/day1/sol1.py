with open("test.txt","r") as f:
    input = f.readline()

floor = 0
index = 0
while floor != -1:
    if input[index] == "(":
        floor += 1
    elif input[index] == ")":
        floor -= 1
    index += 1

print(index)
