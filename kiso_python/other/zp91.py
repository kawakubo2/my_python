# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:22:57 2017

@author: tomok
"""

uppers = [4.23, 2.32, 5.862, 3.0, 2.98, 7.72]
lowers = [8, 7, 3, 2, 1, 9]
heights = [5, 5, 3, 2, 1, 6]

for upper, lower, height in zip(uppers, lowers, heights):
    print("上辺が{}cm、下辺が{}cm、高さが{}cmの台形の面積は{:.2f}平方cmです"
          .format(upper, lower, height,(upper + lower) * height / 2))
    print("上辺が" + str(upper) + "cm、下辺が" + str(lower) 
            + "cm、高さが" + str(height)
           + "cmの台形の面積は" + str((upper + lower) * height / 2) + "平方cmです")