# from collections import deque
#
# def find_min_steps(start_molecule):
#     visited = set()
#     queue = deque([(start_molecule, 0)])
#
#     while queue:
#         current, steps = queue.popleft()
#         print(current, steps)
#         if current == 'e':
#             return steps
#         for neighbor in shiftings(current):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append((neighbor, steps + 1))
#     return -1

def determine_smallest_distance(molecule):
    global transformations

    if molecule == 'e':
        return 0

    possible_shiftings = shiftings(molecule)

    min_cost_next = 999999999
    for x in possible_shiftings:
        cost_next = determine_smallest_distance(x)
        if cost_next < min_cost_next:
            min_cost_next = cost_next

    print(1 + min_cost_next)
    return 1 + min_cost_next

def shiftings(molecule):
    global transformations

    shifting = set()

    for i in transformations:
        for j in range(len(molecule)-len(i[1])+1):
            if molecule[j:j+len(i[1])] == i[1]:
                shifting.add(molecule[:j] + i[0] + molecule[j+len(i[1]):])

    return shifting

with open("input.txt") as f:
    x = f.readline().strip()
    transformations = []
    while x != "":
        transformations.append(x.split(" => "))
        x = f.readline().strip()
    molecule = f.readline().strip()

print(determine_smallest_distance(molecule))
