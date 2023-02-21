from calendar import TextCalendar

cal = TextCalendar(6)

cal_dict = {}
for year in range(2000, 2101):
    for month in range(1, 13):
        cal_dict[(year, month)] = cal.formatmonth(year, month)

while True:
    s = input('年を入力してください(終了はq): ')
    if s == 'q':
        break
    year = int(s)
    month = int(input('月を入力してください: '))
    print(cal_dict.get((year, month)))