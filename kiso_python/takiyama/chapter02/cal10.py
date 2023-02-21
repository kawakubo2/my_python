from calendar import TextCalendar, firstweekday

def printcalheader(year, month):
    print(f"      {year}年{month}月   ")

def getweekdaylist(firstweekday):
    weekday_list = ["月","火","水","木","金","土","日"]
    for i in range(0, len(weekday_list) - firstweekday):
        w = weekday_list.pop();
        weekday_list.insert(0, w)
    return weekday_list

def printweekday(firstweekday):
    for w in getweekdaylist(firstweekday):
        print(f"{w} ", end="")
    print()

def print_ja_calendar(year, month, firstweekday = 0):
    cal = TextCalendar(firstweekday)
    cal_str = cal.formatmonth(year, month)
    cal_list = cal_str.split("\n")
    printcalheader(year, month)
    printweekday(cal.getfirstweekday())
    for i in range(2, len(cal_list)):
        print(cal_list[i])


if __name__ == '__main__':
    year = int(input("年: "))
    month = int(input("月: "))
    print_ja_calendar(year, month, 6)