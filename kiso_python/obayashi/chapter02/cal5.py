from calendar import TextCalendar

cal = TextCalendar(6)
month = []
for m in range(1,13):
    month.append(cal.formatmonth(2021,m))

while True:
    tuki = int(input('月(0で終了): '))
    if tuki == 0: break
    print(month[tuki-1])

