from calendar import TextCalendar

day_of_weeks = [
    '月 火 水 木 金 土 日',
    '火 水 木 金 土 日 月',
    '水 木 金 土 日 月 火',
    '木 金 土 日 月 火 水',
    '金 土 日 月 火 水 木',
    '土 日 月 火 水 木 金',
    '日 月 火 水 木 金 土'
]

year = int(input('年: '))
month = int(input('月: '))
firstdayofweek = int(input('何曜始まり?(0.月～6.日): '))
cal = TextCalendar(firstdayofweek)
cal_str = cal.formatmonth(year, month)
print(cal_str)

cal_list = cal_str.split('\n')
cal_list[0] = f'     {year}年{month}月'
cal_list[1] = day_of_weeks[firstdayofweek]
cal_str = '\n'.join(cal_list)
print(cal_str)
