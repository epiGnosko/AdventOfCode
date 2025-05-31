def calcdist(speed, time, rest, optime):
    dist = 0
    complete_iterations = optime // (time + rest)
    dist += speed * time * complete_iterations
    remaining = optime - (time + rest) * complete_iterations
    dist += speed * min(time, remaining)
    return dist

with open("processed_input.txt") as f:
    input = f.readlines()

max_distance = 0
for i in input:
    i = i.strip().split(" ")
    speed = int(i[1])
    time = int(i[2])
    rest = int(i[3])
    distance = calcdist(speed, time, rest, 2503)
    if distance > max_distance:
        max_distance = distance

print(max_distance)
