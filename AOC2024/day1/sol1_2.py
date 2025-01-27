with open("text1.txt") as f:
    inp = f.readlines()

lst1 = []
lst2 = []
for i in inp:
    lst1.append(int(i.split("   ")[0]))
    lst2.append(int(i.split("   ")[1].strip()))

lst1.sort()
lst2.sort()

similarity_score = 0

for i in lst1:
    count = 0
    for j in lst2:
        if i == j:
            count += 1
    similarity_score += i*count

print(similarity_score)
