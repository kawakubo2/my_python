# -*- coding: utf-8 -*-
class Rectangle:
    def __init__(self, width, height):
        self.set_width(width)        
        self.set_height(height)
        
    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        if width <= 0:
            raise ValueError("値が負")
            
        self.__width = width
        
    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        if height <= 0:
            raise ValueError("値が負")
            
        self.__height = height
        
    def area(self):
        return self.__width * self.__height
    
    def diagonal(self):
        import math
        return math.sqrt(self.__width ** 2 + self.__height ** 2)
    
rects = [(3, 4), (-6, 8), (5, 12)]

area_total = 0

try:
    for rect in rects:
        rec = Rectangle(rect[0], rect[1])
        area_total += rec.area()
        print("面積:{:.1f} 対角線:{:.1f}".format(rec.area(), rec.diagonal()))
    
    print("合計面積:{:.1f}".format(area_total))
except ValueError:
    print("xxxx")