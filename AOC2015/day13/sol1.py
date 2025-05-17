from io import BufferedIOBase
import itertools

people = (
    "Alice",
    "Bob",
    "Carol",
    "David",
    "Eric",
    "Frank",
    "George",
    "Mallory",
)

chart = {}

with open("processed_input.txt") as f:
    input = f.readlines()
    for i in input:
        i = i.strip().split(" ")
        if i[0] not in chart:
            chart[i[0]] = {}
        if i[1] == "+":
            chart[i[0]][i[3]] = int(i[2])
        else: 
            chart[i[0]][i[3]] = -int(i[2])

max_happiness = 0
for i in itertools.permutations(people):
    happiness = 0
    for j in range(len(i)):
        happiness += chart[i[j]][i[j-1]]
        happiness += chart[i[j]][i[(j+1) % len(i)]]
    if happiness > max_happiness:
        max_happiness = happiness

print(max_happiness)

