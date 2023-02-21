# -*- coding: utf-8 -*-

total = 0

def add(n):
    global total
    total += n
    
def sub(n):
    global total
    total -= n
    
def mul(n):
    global total
    total *= n
    
def div(n):
    global total
    total /= n
    
add(1000)
print("total=", total)
sub(200)
print("total=", total)
mul(2)
print("total=", total)
div(4)
print("total=", total)

print('a', end='')
print('b')