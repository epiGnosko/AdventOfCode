with open("test.txt","r") as f:
    input = f.readline()

floor = 0
for i in input:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1

print(floor)
