def isnotlegal(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[j] not in rules[x[i]]:
                return True
    return False

def correct(x):
    for i in range(len(x)-1):
        if x[i+1] not in rules[x[i]]:
            pass

with open("test.txt") as f:
    inp = f.readlines()

rules = {}

i = 0
while "|" in inp[i]:
    nums = inp[i].strip().split("|")
    if nums[0] not in rules:
        rules[nums[0]] = {}
    rules[nums[0]][nums[1]] = True
    i += 1

i += 1
answer = 0

while i < len(inp):
    nums = inp[i].split(",")
    nums[-1] = nums[-1].strip()
    if isnotlegal(nums) and nums[len(nums)//2] != '':
        correct(nums)
        answer += int(nums[len(nums)//2])
    i += 1

print(answer)
