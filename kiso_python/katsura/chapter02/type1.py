# 動的型付け言語
n = 10
print(type(n))
if type(n) == int:
    print('nはint型')

n = 'abc'
print(type(n))

n = True
print(type(n))

def add(x, y):
    return x + y

n = add
print(type(n))
print(n(100, 200))

a = 1_000_000
b = 1_000_000_000

c = a * b
print(f"{c}={a}*{b}")

f = 3.51378e10
g = 1.23e-9

s = "He's a teacher."
print(s)
s = 'He is "GREAT" teach'
print(s)
s = 'He\'s \t\t\t\t"GREAT"\n teacher.'
print(s)
print('caf\u00E9')
print('\u0604')

color = "#FC1B3D"
r = color[1:3]
g = color[3:5]
b = color[5:7]
print(f"r={int(r, 16)}, g={int(g, 16)}, b={int(b, 16)}")
bits = "1111011010101010100001010111"
print(int(bits, 2))