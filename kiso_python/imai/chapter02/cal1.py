# -*- coding: utf-8 -*-

import calendar

cal = calendar.TextCalendar(firstweekday = 6)
cal.prmonth(2020, 6)

cal.pryear(2021)

cal.setfirstweekday(0)
cal.prmonth(2020, 6)

# help(calendar.TextCalendar)