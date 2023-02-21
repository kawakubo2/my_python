# -*- coding: utf-8 -*-

from calendar import TextCalendar

cal = TextCalendar(6)

year = 2020

month_list = []

for month in range(1, 13):
    month_list.append(cal.formatmonth(year, month))
    

for i in range(12):
    print(month_list[i])
    