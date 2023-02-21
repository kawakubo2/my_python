from calendar import TextCalendar

year = 2022
month = 12

day = 3
cal = TextCalendar(day)
cal_str = cal.formatmonth(year, month)
cal_list = cal_str.split("\n")
cal_list[0] = f"      {year}年{month}月"
print(cal_list)
youbi_list = ['月', '火', '水', '木', '金', '土', '日']

youbi = []
for i in range(7):
    youbi.append(f"{youbi_list[day]}")
    day = (day + 1) % 7
    
cal_list[1] = " ".join(youbi)

cal_str = "\n".join(cal_list)
print(cal_str)