from calendar import TextCalendar

day = 3
cal = TextCalendar(day)
# year = int(input("年: "))
# month = int(input("月: "))
year = 2022
month = 11
cal_str = cal.formatmonth(year, month)
cal_list = cal_str.split('\n')
# print(cal_list)
print("     " + str(year) + "年" + str(month) + "月")
dow = ['月', '火', '水', '木', '金', '土', '日']
for _ in range(len(dow)):
    print(dow[day] + " ", end="")
    day += 1
    day = day % 7
print()
for n in range(2, len(cal_list)):
    print(cal_list[n])