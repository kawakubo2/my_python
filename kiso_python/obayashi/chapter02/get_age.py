import datetime

def get_age(year, month, day):
    today = datetime.datetime.today()
    age = today.year - year
    if (month, day) > (today.month, today.day):
        age -= 1
    return age

print(get_age(2000, 3, 22))

age = int(input("年齢を入力してください: "))
if age < 0:
    print("正数を入力してください")
elif age < 3:
    print("無料です")
elif age < 13:
    print("200円です")
elif age < 65:
    print("400円です")
else:
    print("無料です")