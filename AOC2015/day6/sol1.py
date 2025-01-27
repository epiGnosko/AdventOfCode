def display_lights():
    for row in lights:
        for element in row:
            print(element,end="")
        print()

def toggle(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            if lights[i][j] == ".":
                lights[i][j] = "@"
            else:
                lights[i][j] = "."

def turnOn(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] = "@"

def turnOff(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] = "."


with open("input.txt") as f:
    input = f.readlines()

row = ["."] * 1000
lights = []
for i in range(1000):
    lights.append(row.copy())

for i in input:
    nums = i.split(',')
    a = int(nums[0].split(' ')[-1])
    b = int(nums[1].split(' ')[0])
    x = int(nums[1].split(' ')[-1])
    y = int(nums[2])
    if "on" in i:
        turnOn(a,b,x,y)
    elif "off" in i:
        turnOff(a,b,x,y)
    else:
        toggle(a,b,x,y)

lit = 0
for i in lights:
    for j in i:
        if j == "@":
            lit += 1

print(lit)
