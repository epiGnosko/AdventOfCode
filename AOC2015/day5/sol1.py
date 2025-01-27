def isNice(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    forbidden = ['ab', 'cd', 'pq', 'xy']
    adjacent = False
    for i in forbidden:
        if i in x:
            return False
    for i in range(len(x)):
        if x[i] in vowels:
            vowel_count += 1
        if i < len(x)-1 and x[i+1] == x[i]:
            adjacent = True
    if vowel_count > 2 and adjacent:
        return True
    return False


with open("input.txt","r") as f:
    input = f.readlines()

nice_lines = 0
for i in input:
    if isNice(i):
        nice_lines += 1
print(nice_lines)
