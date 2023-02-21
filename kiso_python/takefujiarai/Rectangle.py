# -*- coding: utf-8 -*-

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def diagonal(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def distance(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    

r1 = Rectangle(8, 6, 3, 4)
r2 = Rectangle(5, 3, 3.331, 8.831)

print('r1 面積{:.1f}'.format(r1.area()))
print('r1 対角線{:.1f}'.format(r1.diagonal()))
print('r1 原点からの距離{:.1f}'.format(r1.distance()))