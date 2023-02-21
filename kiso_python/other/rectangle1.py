# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:27:01 2017

@author: tomok
"""
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def diagonal(self):
        return math.sqrt(math.pow(self.width, 2) + math.pow(self.height, 2))
        

    
r1 = Rectangle(8, 5)
print("面積:", r1.area())
print("対角線:", r1.diagonal())

r2 = Rectangle(12.3253, 5.5151)
print("面積:", r2.area())
print("対角線:", r2.diagonal())