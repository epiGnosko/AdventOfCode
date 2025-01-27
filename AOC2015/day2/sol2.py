def getsides(x):
    a, b, c = x.strip().split("x")

    return int(a), int(b), int(c)

def getlen(a,b,c):
    bow = a*b*c
    loop = 2*min(a+b, b+c, c+a)

    return bow + loop


with open("test.txt","r") as f:
    input = f.readlines()

ribbon = 0
for i in input:
    x, y, z = getsides(i)
    ribbon += getlen(x, y, z)

print(ribbon)
