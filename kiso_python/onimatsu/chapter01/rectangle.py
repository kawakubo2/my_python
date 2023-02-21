# -*- coding: utf-8 -*-
import math

class Rectangle:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return (self.width + self.height) * 2
    
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)