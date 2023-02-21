# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:39:14 2017

@author: tomok
"""
import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

r1 = Rectangle(4, 3)
print("面積:" + str(r1.area()))
print("外周:" + str(r1.perimeter()))
print("対角線:" + str(r1.diagonal()))
