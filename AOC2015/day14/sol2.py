def calcdist(speed, time, rest, optime):
    dist = 0
    complete_iterations = optime // (time + rest)
    dist += speed * time * complete_iterations
    remaining = optime - (time + rest) * complete_iterations
    dist += speed * min(time, remaining)
    return dist

with open("processed_input.txt") as f:
    input = f.readlines()
    data = []
    for i in range(len(input)):
        data.append(input[i].strip().split(" "))
        data[-1][1] = int(data[-1][1])
        data[-1][2] = int(data[-1][2])
        data[-1][3] = int(data[-1][3])

points = {}

for i in range(1,2504):
    max_distance = 0
    for j in data:
        distance = calcdist(j[1],j[2],j[3],i)
        if distance > max_distance:
            max_distance = distance
    for j in data:
        distance = calcdist(j[1],j[2],j[3],i)
        if distance == max_distance:
            if j[0] in points:
                points[j[0]] += 1
            else:
                points[j[0]] = 1

most_points = 0
for i in points:
    if points[i] > most_points:
        most_points = points[i]

print(most_points)
