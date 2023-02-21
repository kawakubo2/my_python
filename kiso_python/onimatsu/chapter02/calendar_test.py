# -*- coding: utf-8 -*-

from calendar import TextCalendar

help(TextCalendar)

cal = TextCalendar()

cal.prmonth(2019, 3)

cal2 = TextCalendar(firstweekday=6)
cal2.prmonth(2019, 3)

# cal3 = LocaleTextCalendar()
# cal3.prmonth(2019, 3)
