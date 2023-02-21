import math, cmath
x = 0.2
y = 0.6

DELTA = 1.0e-9

print(x * 3)
if abs(x * 3 - y) < DELTA:
    print('○')
else:
    print('×')

x = 1 
while x <= 100:
    print(f'{x / 100:.2f}')
    x = x + 1

print(cmath.sqrt(-1))