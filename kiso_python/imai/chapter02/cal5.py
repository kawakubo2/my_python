# -*- coding: utf-8 -*-

from calendar import TextCalendar

year = int(input('年を入力してください: '))
month = int(input('月を入力してください: '))

cal = TextCalendar(6)

cal_str = cal.formatmonth(year, month)

print(cal_str)

ja_wdays = "日 月 火 水 木 金 土"

cal_array = cal_str.split("\n")
cal_array[1] = ja_wdays
cal_str = "\n".join(cal_array)
print(cal_str)