# -*- coding: utf-8 -*-

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

a = 5
b = 3
c = 9

# a + (b * c) / a
answer = div(add(a, mul(b, c)), a)
print(answer)