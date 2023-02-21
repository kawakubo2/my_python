# -*- coding: utf-8 -*-

from calendar import TextCalendar
from calendar import HTMLCalendar

year = int(input('年を入力してください: '))
month = int(input('月を入力してください: '))

cal = TextCalendar(6)
cal.prmonth(year, month)

#cal2 = HTMLCalendar(6)
#s = cal2.formatmonth(2020, 7)
#print(s)