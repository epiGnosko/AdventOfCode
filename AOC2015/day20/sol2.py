def numberofpresents(house):
    num = house
    presents = 0
    div = 0
    while div < 50:
        div += 1
        if num % div == 0:
            presents += num / div * 11
    return presents

start = 1
presents = numberofpresents(start)
while presents != 29000000:
    print(f"House {start} got {presents} presents")
    start += 1
    presents = numberofpresents(start)
    if presents > 29000000:
        print("not exact")
        break

print(start)
