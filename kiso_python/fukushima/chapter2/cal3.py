# -*- coding: utf-8 -*-

from calendar import TextCalendar , HTMLCalendar

cal = TextCalendar(6)
cal.prmonth(2020, 8)

cal2 = HTMLCalendar()
cal_str = cal2.formatmonth(2020, 8)
print(cal_str)