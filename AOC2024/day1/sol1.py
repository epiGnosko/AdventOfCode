with open("text1.txt") as f:
    inp = f.readlines()

lst1 = []
lst2 = []
for i in inp:
    lst1.append(int(i.split("   ")[0]))
    lst2.append(int(i.split("   ")[1].strip()))

lst1.sort()
lst2.sort()

difference = 0

for i in range(len(lst1)):
    difference += abs(lst1[i] - lst2[i])

print(difference)
