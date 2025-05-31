with open("input.txt") as f:
    x = f.readline().strip()
    transformations = []
    while x != "":
        transformations.append(x.split(" => "))
        x = f.readline().strip()
    molecule = f.readline().strip()

shiftings = set()

for i in transformations:
    for j in range(len(molecule)-len(i[0])+1):
        if molecule[j:j+len(i[0])] == i[0]:
            shiftings.add(molecule[:j] + i[1] + molecule[j+len(i[0]):])

print(len(shiftings))
