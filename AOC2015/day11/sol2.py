def increment(x):
    if x[-1] == 'z':
        return increment(x[:-1]) + 'a'
    return x[:-1] + chr(ord(x[-1]) + 1)

def has_straight(x):
    for i in range(len(x)-2):
        if ord(x[i]) +1 == ord(x[i+1]) and ord(x[i+1]) +1 == ord(x[i+2]):
            return True
    return False

def contains_forbidden(x):
    for char in x:
        if char == 'i' or char == 'o' or char == 'l':
            return True
    return False 

def has_two_pairs(x):
    count = 0
    i = 0
    while i < len(x) - 1:
        if x[i] == x[i+1]:
            count += 1
            i += 1
        i += 1
    return (count >= 2)

input = "hepxcrrq"

while True:
    input = increment(input)
    if has_straight(input) and not contains_forbidden(input) and has_two_pairs(input):
        break

while True:
    input = increment(input)
    if has_straight(input) and not contains_forbidden(input) and has_two_pairs(input):
        break

print(input)
