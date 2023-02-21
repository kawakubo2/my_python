from math import ceil, floor, sqrt, hypot

x1 = 1.000000001
print(ceil(x1))

x2 = 1.999999999
print(floor(x2))

x3 = -16
x3 = x3 if x3 > 0 else -x3
print(sqrt(x3))

x4 = 38983.183819861
print("{:.15f}".format(sqrt(x4)))
print("{:.15f}".format(x4 ** 0.5))

a = 8
b = 6

print(sqrt(a ** 2 + b ** 2))
print(hypot(a, b))