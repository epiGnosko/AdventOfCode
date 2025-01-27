def display_lights():
    for row in lights:
        for element in row:
            print(element,end="")
        print()

def toggle(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] += 2

def turnOn(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] += 1

def turnOff(a,b,x,y):
    for i in range(a,x+1):
        for j in range(b,y+1):
            lights[i][j] -= 1
            if lights[i][j] < 0:
                lights[i][j] = 0


with open("input.txt") as f:
    input = f.readlines()

row = [0] * 1000
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
        lit += j

print(lit)
