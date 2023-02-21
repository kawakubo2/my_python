# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:01:43 2021

@author: tomok
"""
from calendar import TextCalendar
from math import pow, pi

cal = TextCalendar(6)

cal.prmonth(2021, 2)

radius = 5 # 半径5cm

area = pow(radius, 2) * pi

print(area)