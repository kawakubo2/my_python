from calendar import TextCalendar

year = int(input('年を入力してください: '))
month = int(input('月を入力してください: '))

cal = TextCalendar(firstweekday=6)
cal.prmonth(year, month)