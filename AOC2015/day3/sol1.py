with open("test.txt") as f:
    input = f.readline()
    
current_house = [0,0]

visited_enc = [0]

for i in input:
    if i == "^":
        current_house[1] += 1
    if i == ">":
        current_house[0] += 1
    if i == "<":
        current_house[0] -= 1
    if i == "v":
        current_house[1] -= 1
    
    enc_add = 2**current_house[0] * 3**current_house[1]

    if enc_add not in visited_enc:
        visited_enc.append(enc_add)

print(len(visited_enc))
