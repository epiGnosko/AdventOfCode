# Takes 40s to run on my computer, please be patient 
def numberofpresents(house):
    num = 1
    presents = 0
    while num <= house**0.5:
        num += 1
        if house % num == 0:
            presents += num * 10
            presents += house / num * 10
    presents += house * 10
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
