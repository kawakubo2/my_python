from calendar import TextCalendar

year = 2020
month_list = []
cal = TextCalendar(firstweekday=6)
for n in range(1, 13):
    month_list.append(cal.formatmonth(year, n))

while True:
    month = int(input('月を入力してください(終了の場合は0): '))
    if month == 0:
        break
    print(month_list[month - 1])