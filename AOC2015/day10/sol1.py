def look_and_say(x):
    x = str(x)
    processed = ""
    count = 0
    index = 0
    while index < len(x):
        char = x[index]
        while index < len(x) and x[index] == char :
            count += 1
            index += 1
        processed += str(count) + char
        count = 0
    return processed

def main():
    input = "3113322113"
    for _ in range(40):
        input = look_and_say(input)
    print(len(input))

main()
