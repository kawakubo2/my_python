from calendar import HTMLCalendar, TextCalendar

year = int(input("年を入力してください: "))
month = int(input("月を入力してください: "))

cal = TextCalendar(6)
cal.prmonth(year, month)
cal.setfirstweekday(0)
cal.prmonth(year, month)
