import calendar

cal = calendar.TextCalendar()
cal.prmonth(2020, 8)
cal.pryear(2020)

ja_cal = calendar.LocaleTextCalendar(locale = 'ja_jp')
print(ja_cal.formatmonth(2020, 8))