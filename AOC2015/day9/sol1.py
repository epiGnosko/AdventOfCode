def connect():
    global cost
    min = graph[connections[0][0]][connections[1][0]]
    city1 = connections[0][0]
    city2 = connections[1][0]
    for i in range(len(connections)-1):
        for j in range(i+1, len(connections)):
            ends1 = (connections[i][0], connections[i][-1])
            ends2 = (connections[j][0], connections[j][-1])
            for k in ends1:
                for l in ends2:
                    if min > graph[k][l]:
                        min = graph[k][l]


def fill_values(x:str):
    processed = x.split(" = ")
    city1, city2 = processed[0].split(" to ")
    if city1 not in graph:
        graph[city1] = {}
    if city2 not in graph:
        graph[city2] = {}
    graph[city1][city2] = int(processed[1])

with open("input.txt","r") as f:
    input = f.readlines()

cities = {
    "Tristram" : 0,
    "AlphaCentauri" : 0,
    "Snowdin": 0,
    "Tambi": 0,
    "Faerun": 0,
    "Norrath": 0,
    "Straylight":0,
    "Arbre": 0,
}

connections = [[x] for x in cities]

graph = {}
cost = 0
for i in input:
    fill_values(i)

while len(connections) > 1:
    connect()

print(cost)
