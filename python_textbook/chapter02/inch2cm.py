# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:12:08 2017

@author: tomok
"""

per_inch = 2.54
inch = float(input('インチ： '))
print("{:.1f}インチは{:.3f}cmです".format(inch, inch * per_inch))

