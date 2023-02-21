def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def last_of_month(year, month):
    months = [
        [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ],
        [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ],
    ]
    return months[1 if is_leap_year(year) else 0][month]

year = int(input("年を入力してください: "))
month = int(input("月を入力してください: "))

print("{}年{}月の月末は{}日です。".format(year, month, last_of_month(year, month)))