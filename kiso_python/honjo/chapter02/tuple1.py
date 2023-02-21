# -*- coding: utf-8 -*-

height = (182, 165, 159, 171, 155)

print(height[0])
print(height[1])
print(height[2])
print(height[3])
print(height[4])

height2 = list(height)
height2[0] = 185
print(height2)

name = "川久保智晴"

for s in name:
    print(s)
    
for h in height2:
    print(h)
    
x = 10
print(x.bit_length())

print(id(3))

x = 3
print(id(x))

print(id(name))

def add(x, y):
    return x + y

print(add(100, 200))


class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def diagonal(self):
        from math import sqrt, pow
        return sqrt(pow(self.width, 2) + pow(self.height, 2))

r1 = Rectangle(3, 4)
print(r1.diagonal())
print(r1.diagonal())