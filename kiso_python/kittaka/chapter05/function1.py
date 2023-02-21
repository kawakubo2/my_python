def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

# (a + b) * (a - c) - c
# (8 + 4) * (8 - 3) - 3
# 12 * 5 - 3 ---> 57
a = 8
b = 4
c = 3
answer = sub(mul(add(a, b), sub(a, c)), c)
print(f"答え: {answer}")
