# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 01:12:24 2017

@author: tomoharu
"""

points = [80, 40, 23, 14, 29, 58]

akaten = []

for point in points:
    if point < 30:
        akaten.append(point)
        
print(akaten)
