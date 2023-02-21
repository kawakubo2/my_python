from string_calendar import StringCalendar

cal = StringCalendar()

for y in (2012, 2015, 2017):
    for m in range(6, 9):
        print(cal.prmonth(y, m))