def add(a, b):
    return a + b

def sub(a, b):
    return a- b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


x = 10
y = 20
z = 30

# ((x - y) * (x + y)) / z
answer = div((mul(sub(x, y), add(x, y))), z)

print('((x - y) * (x + y)) / z =', answer)
print('abc', end='')
print('x', 'y', 1, 2, 3, sep='-')

a = "12.34"
b = float(a)

if b > 10:
    print('大きい')
elif b < 10:
    print('小さい')
else:
    print('等しい')

12 + 34.22 - 3.23 * 38