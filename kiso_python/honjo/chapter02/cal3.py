# -*- coding: utf-8 -*-

from calendar import TextCalendar

cal = TextCalendar(6)
cal.prmonth(2020, 7)

year2018 = cal.formatyear(2018)

print(year2018)