# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:13:50 2017

@author: tomok
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def getArea(self):
        return self.width * self.height
