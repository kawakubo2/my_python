# -*- coding: utf-8 -*-

x = 10
y = 10.2
s = 'abc'

print(type(x))
print(type(y))
print(type(s))

def add(a, b):
    return a + b

print(add)

z = add
print(z(10, 30))