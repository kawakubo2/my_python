# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:31:19 2017

@author: tomok
"""

weekdays = ['日', '月', '火', '水', '木', '金', '土']

weekdays.reverse()
print(weekdays)

weekdays.reverse()
print(weekdays)

weekdays2 = weekdays[::-1]
print(weekdays)
print(weekdays2)
weekdays2[0] = '天'
print(weekdays)
print(weekdays2)
