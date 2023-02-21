def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# (4 * (5 - 3)) / (7 - 2)
answer = div(mul(4, sub(5, 3)), sub(7, 2))
print(answer)

def fukuri(ganpon, nenri, nen):
    result = ganpon
    for i in range(nen):
        result *= (1 + nenri)
    return result

print(fukuri(10000, 0.1, 70))