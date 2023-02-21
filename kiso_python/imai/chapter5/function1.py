def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def print_add(a, b):
    print('{} + {} = {}'.format(a, b, a + b))
    
x = 10
y = 20
z = 15

# (x + y) * (z - x)
answer = mul(add(x, y), sub(z, x))

print('({} + {}) * ({} - {}) = {}'.format(x, y, z, x, answer))
print(print_add(x, y))