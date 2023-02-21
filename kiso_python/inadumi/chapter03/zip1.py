# -*- coding: utf-8 -*-

weekday1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(weekday1, weekday2):
    print(en + ': ' + ja)
    
upper_bases = [1.23, 5.32, 4.1,   3.5]
lower_bases = [2.23, 7,98, 5.13,  7.71]
heights     = [1.57, 6.48, 6.231, 5.35]

for upper_base,lower_base,height in zip(upper_bases,lower_bases,heights):
    print('台形の面積: ' +\
          str((upper_base + lower_base) * height / 2))