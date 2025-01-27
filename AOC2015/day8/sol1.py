def differs_by(x:str)->int:
    original = len(x)
    in_mem = len(x)-2
    i = 1
    while i < len(x)-1:
        if x[i] == "\\":
            if x[i+1] == "x":
                in_mem -= 3
                i += 3
            else:
                in_mem -= 1
                i += 1
        i += 1
    print(x, "differs_by", original - in_mem)
    return original - in_mem
with open("input.txt") as f:
    input = f.readlines()

difference = 0
for i in input:
    difference += differs_by(i.strip())

print(difference)
