# -*- coding: utf-8 -*-

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y;


x = 5
y = 4
z = 3

# (x + y) * (x - z)
answer = mul(add(x, y), sub(x, z))
print(answer)