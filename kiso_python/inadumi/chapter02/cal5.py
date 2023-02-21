# -*- coding: utf-8 -*-

from calendar import TextCalendar

cal = TextCalendar(6)

year = int(input('年を入力してください:'))
month = int(input('月を入力してください:'))

cal_str = cal.formatmonth(year, month)

with open('cal.txt', 'w', encoding='utf_8') as f:
    f.writelines(cal_str)
