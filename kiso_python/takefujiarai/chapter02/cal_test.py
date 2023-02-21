# -*- coding: utf-8 -*-

from calendar import TextCalendar

cal = TextCalendar()

year = 2019
months = []

for i in range(12):
    months.append(cal.formatmonth(year,i + 1))
    

while(True):
    month = int(input('月を入力してください(終了は0): '))
    if month == 0:
        break
    print(months[month - 1])
    
