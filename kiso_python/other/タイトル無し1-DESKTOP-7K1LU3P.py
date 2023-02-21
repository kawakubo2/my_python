# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:22:57 2017

@author: tomok
"""

uppers = [4, 2, 5, 3, 2, 7]
lowers = [8, 7, 3, 2, 1, 9]
heights = [5, 4, 3, 2, 1, 6]

for upper, lower, height in zip(uppers, lowers, heights):
    print("上辺が{}cm、下辺が{}cm、高さが{}cmの台形の面積は{:.2f}平方cmです"
          .format(upper, lower, height,(upper + lower) * height / 2))
    print("上辺が" + upper + "cm、下辺が" + lower + "cm、高さが" + height
           + "cmの台形の面積は" + ((upper + lower) * height / 2) + "平方cmです")