def getsides(x):
    a, b, c = x.strip().split("x")

    return int(a), int(b), int(c)

def getarea(a,b,c):
    surface_area = 2*a*b + 2*b*c + 2*c*a
    slack = min(a*b, b*c, c*a)

    return surface_area + slack


with open("test.txt","r") as f:
    input = f.readlines()

paper = 0
for i in input:
    x, y, z = getsides(i)
    paper += getarea(x, y, z)

print(paper)
