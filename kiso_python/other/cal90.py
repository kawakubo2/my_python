# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:44:10 2017

@author: tomok
"""

from calendar import TextCalendar

month_list = []

cal = TextCalendar(6)
year = 2017
for n in range(1, 13):
    month_list.append(cal.formatmonth(year, n))

month = int(input("月を指定してください: "))
print(month_list[month - 1])