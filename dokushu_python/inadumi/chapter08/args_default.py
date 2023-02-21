def func1(unit_price, quantity, c = 0):
    return unit_price * quantity * (1 - c)

print(func1(1000, 30))
print(func1(1000, 30, 0.3))

def func2(a, b, c = None):
    if c is None:
        c = []
    c.append(a)
    c.append(b)
    return c

print(func2('a', 'b'))
print(func2('c', 'd'))
print(func2('e', 'f', ['x', 'y', 'z']))