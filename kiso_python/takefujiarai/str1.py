# -*- coding: utf-8 -*-

weekday = '日月火水木金土'

for day in weekday:
    print(day + '曜日')
    
weekday2 = [c + '曜日' for c in weekday]
print(weekday2)