from calendar import TextCalendar

month_list = []

cal = TextCalendar(6)

year = 2021
for month in range(1, 13):
    str1 = cal.formatmonth(year, month)
    list1 = str1.split("\n")
    pre1 = "     {}年 {}月".format(year, month)
    pre2 = "日 月 火 水 木 金 土"
    list1[0] = pre1
    list1[1] = pre2
    month_list.append("\n".join(list1))

while True:
    m = int(input('月(0で終了): '))
    if m == 0:
        break
    print(month_list[m - 1])