def hasTwinPair(x):
    for i in range(len(x)-1):
        if x[i:i+2] in x[i+2:]:
            return True
    return False

def hasTwinChar(x):
    for i in range(len(x)-2):
        if x[i] == x[i+2]:
            return True
    return False

def isNice(x):
    return hasTwinPair(x) and hasTwinChar(x)


with open("input.txt","r") as f:
    input = f.readlines()

nice_lines = 0
for i in input:
    if isNice(i):
        nice_lines += 1
print(nice_lines)
