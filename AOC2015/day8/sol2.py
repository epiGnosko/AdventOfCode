def differs_by(x:str)->int:
    difference = 2
    for i in x:
        if i in ("\\","\""):
            difference += 1
    return difference
with open("input.txt") as f:
    input = f.readlines()

difference = 0
for i in input:
    difference += differs_by(i.strip())

print(difference)
