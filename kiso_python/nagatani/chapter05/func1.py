"""
x, yを仮引数(parameter)と呼ぶ
"""
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

# (a + b) * (a - c) / d

a = 10
b = 8
c = 4
d = 5

answer = div(mul(add(a, b), sub(a, c)), d)
print(answer)

def dollar_to_yen(dollar, rate):
    return dollar * rate

d = 100
r = 105
print(dollar_to_yen(d, r))

print(dollar_to_yen(rate=150, dollar=200))