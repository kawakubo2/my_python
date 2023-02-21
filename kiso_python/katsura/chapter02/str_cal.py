# str_cal.py
from calendar import TextCalendar

START_YEAR = 1901
END_YEAR   = 2100

cal = TextCalendar(6)

cal_dict = {}
for year in range(START_YEAR, END_YEAR + 1):
    for month in range(1, 13):
#        cal_dict[(year, month)] = cal.formatmonth(year, month)
        temp = cal.formatmonth(year, month).split("\n")
        temp[1] = "日 月 火 水 木 金 土"
        ja_week = "\n".join(temp)
        cal_dict[(year, month)] = ja_week

while True:
    s = input('年(終了時はq): ')
    if s == 'q':
        break
    y = int(s)
    m = int(input('月: '))
    print(cal_dict[(y, m)])