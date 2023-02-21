from calendar import TextCalendar

year = int(input('年: '))
month = int(input('月: '))

cal = TextCalendar(6)
cal.prmonth(year, month)