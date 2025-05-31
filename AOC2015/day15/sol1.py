def vector_add(a, b):
    x = []
    for i in range(len(a)):
        x.append(a[i] + b[i])
    return x

def scalar_mult(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i] * y)
    return z

def total_score(x):
    score = 1 
    for i in range(len(x)-1):
        score *= max(x[i],0)
    return score


with open("processedinput.txt") as f:
    inputdata = f.readlines()

ingredients = {}

for i in inputdata:
    data = i.strip().split(" ")
    for i in range(1, len(data)):
        data[i] = int(data[i])
    ingredients[data[0]] = data[1:]

max_num = [0, 0, 0, 0, 0]

for i in range(101):
    for j in range(101):
        for k in range(101):
            if (i+j+k > 100):
                continue
            net = [0] * 5
            net = vector_add(net, scalar_mult(ingredients["Sugar"], i))
            net = vector_add(net, scalar_mult(ingredients["Sprinkles"], j))
            net = vector_add(net, scalar_mult(ingredients["Candy"], k))
            net = vector_add(net, scalar_mult(ingredients["Chocolate"], 100 - (i+j+k)))
            if total_score(net) > max_num[0]:
                max_num = [total_score(net), i, j, k, 100 - (i + j + k)]

print(max_num)
