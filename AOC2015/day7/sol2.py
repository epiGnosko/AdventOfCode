def evaluate(s: str) -> int:
    if s in cache:
        return cache[s];
    if s.isnumeric():
        return int(s)
    elif "AND" in signals[s]:
        num1, num2 = signals[s][0], signals[s][-1]
        cache[s] = evaluate(num1) & evaluate(num2)
        return cache[s]
    elif "OR" in signals[s]:
        num1, num2 = signals[s][0], signals[s][-1]
        cache[s] = evaluate(num1) | evaluate(num2)
        return cache[s]
    elif "NOT" in signals[s]:
        num = signals[s][-1]
        cache[s] = ~evaluate(num) & 65535
        return cache[s]
    elif "RSHIFT" in signals[s]:
        num1, num2 = signals[s][0], signals[s][-1]
        cache[s] = evaluate(num1) >> evaluate(num2)
        return cache[s]
    elif "LSHIFT" in signals[s]:
        num1, num2 = signals[s][0], signals[s][-1]
        cache[s] = evaluate(num1) << evaluate(num2)
        return cache[s]
    cache[s] = evaluate(signals[s][0])
    return cache[s]


with open("input.txt") as f:
    input = f.readlines()

signals = {}
cache = {}
for i in input:
    signal, wire = i.strip().split("->")
    signals[wire.strip()] = signal.strip().split(" ")

signals['b'] = [str(evaluate("a"))]
cache.clear()
print(evaluate("a"))
