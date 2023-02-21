# -*- coding: utf-8 -*-
from calendar import TextCalendar

cal = TextCalendar(6)

year = int(input('年を入力してください: '))

month_ary = []
for m in range(12):
    month_ary.append(cal.formatmonth(year, m+1))

# =============================================================================
# print(month_ary)  
# =============================================================================
while True:
    month = int(input('月を入力してください(終了の場合99): '))
    if month == 99:
        break
    print(month_ary[month-1])
