def connect():
    global cost
    min = graph["Tristram"]["AlphaCentauri"]
    city1 = "Tristram"
    city2 = "AlphaCentauri"
    for i in graph:
        for j in graph[i]:
            if i != j and min > graph[i][j]:
                city1 = i
                city2 = j 
                min = graph[i][j]
    if cities[city1] + cities[city2] < 2:
        print(city1 + " to " + city2 + " takes", graph[city1][city2])
        cities[city1] += 1
        cities[city2] += 1
        cost += min 
    del graph[city1][city2]

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

graph = {}
cost = 0
for i in input:
    fill_values(i)

for i in graph:
    print(i ,"-> ", graph[i])

while True:
    ones = 0
    twos = 0
    for i in cities:
        if cities[i] == 1:
            ones += 1
        if cities[i] == 2:
            twos += 1
    if ones == 2 and twos == 6:
        break
    connect()

print(cost)
