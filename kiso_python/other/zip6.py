# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:25:03 2017

@author: tomok
"""

week_en = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
week_ja = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(week_en, week_ja):
    print("{}:{}".format(en, ja))
    
uppers = [2, 5, 4, 6]
lowers = [6, 2, 1, 3]
heights = [4, 2, 1, 6]

for upper, lower, height in zip(uppers, lowers, heights):
    print("上底が{}cm、下底が{}cm、高さが{}cmの台形の面積は{}平方cmです。".format(upper, lower, height, (upper + lower) * height / 2))
