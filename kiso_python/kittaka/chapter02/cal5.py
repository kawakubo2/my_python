from calendar import TextCalendar

year = 2022
month = 4

cal = TextCalendar(2)
cal_str = cal.formatmonth(year, month)
cal_list = cal_str.split("\n")

youbi = ['月', '火', '水', '木', '金', '土', '日']
firstweekday = cal.getfirstweekday()
for i in range(0, 7 - firstweekday):
    youbi.insert(0, youbi.pop())

print(f"     {year}年{month}月")
for y in youbi:
    print(y + " ", end="")
print()

for i in range(2, len(cal_list)):
    print(cal_list[i])