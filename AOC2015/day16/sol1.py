def build_current_sue(x):
    data = x.strip().split(" ")
    sue = {}
    for i in range(2, len(data), 2):
        sue[data[i][:-1]] = data[i+1][:-1]
    return sue

with open("input.txt") as f:
    input_data = f.readlines();

target_sue = {
    "children" : "3",
    "cats" : "7",
    "samoyeds" : "2",
    "pomeranians" : "3",
    "akitas" : "0",
    "vizslas" : "0",
    "goldfish" : "5",
    "trees" : "3",
    "cars" : "2",
    "perfumes" : "1",
}

for i in input_data:
    # print("Sue",i.split(" ")[1][:-1])
    current_sue = build_current_sue(i)
    found = True
    for j in current_sue:
        # print(j, current_sue[j], target_sue[j])
        if current_sue[j] != target_sue[j]:
            found = False
            break
    if found:
        print("Sue Found: ", i.split(" ")[1][:-1])
