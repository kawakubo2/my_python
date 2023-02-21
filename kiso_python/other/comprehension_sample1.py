# -*- coding: utf-8 -*-
"""
Created on Sun May  7 13:58:00 2017

@author: tomok
"""
import math

radiuses = [1, 2, 3, 4, 5]

for area in [r**2*math.pi for r in radiuses]:
    print(area)
