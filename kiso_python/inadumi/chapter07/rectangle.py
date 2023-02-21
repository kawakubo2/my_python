# -*- coding: utf-8 -*-


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return (self.width + self.height) * 2
    
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    
rectangles = [Rectangle(10, 10), Rectangle(20, 5), Rectangle(8, 6)]

for rec in rectangles:
    print("面積:{:7.2f} 外周:{:7.2f} 対角線:{:7.2f}".format(rec.area(), rec.circumference(), rec.diagonal()))