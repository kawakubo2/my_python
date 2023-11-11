from calendar import TextCalendar

year = int(input("年を入力してください: "))
months = []
months.append("")

cal = TextCalendar(6)
for month in range(1, 13):
    months.append(cal.formatmonth(year, month))
    
for month in range(1, 13):
    print(months[month])