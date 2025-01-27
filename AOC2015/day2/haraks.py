total = 0

for line in open('test.txt'):
    l, w, h = line.split('x')
    l, w, h = int(l), int(w), int(h)
    area = 2*l*w + 2*w*h + 2*h*l
    slack = min(l*w, w*h, h*l)
    total += area + slack

print (total)
