def next(active_indices):
    global available_containers
    global target
    if active_indices == []:
        active_indices.append(0)
    elif active_indices[-1] == len(available_containers) - 1:
        if len(active_indices)== 1:
            return False
        active_indices.pop() 
        active_indices.append(active_indices.pop() + 1)
    elif calc_capacity(active_indices) > target:
        active_indices.append(active_indices.pop() + 1)
    else: 
        active_indices.append(active_indices[-1] + 1)
    return True


def calc_capacity(active_indices):
    global available_containers
    capacity = 0
    for i in active_indices:
        capacity += available_containers[i]
    return capacity

with open("input.txt") as f:
    data = f.readlines()

available_containers = []
for i in data:
    available_containers.append(int(i.strip()))

active_indices = []

count = 0
target = 150

hasnext = True
while hasnext:
    for i in active_indices:
        print(available_containers[i], end = " ")
    if calc_capacity(active_indices) == target:
        count += 1 
        print("*", end = " ")
    hasnext = next(active_indices)
    print()

print(count)
