from calendar import TextCalendar

cal = TextCalendar(6)
year = int(input("年: "))
month = int(input("月: "))
cal.prmonth(year, month)