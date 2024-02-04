while True:
    try:
        age = int(input("年齢: "))
        if age < 0:
            print("0以上を入力してください")
            continue
        break
    except ValueError:
        print("数値を入力してください")

while True:
    gender = input("性別 男性:M 女性:F ")
    if gender not in ("M", "F"):
        print("MまたはFを入力してください")
        continue
    break

price = 0
if gender == "M": # 男性の場合
    if age <= 20:
        price = 2400
    elif age <= 50:
        price = 2800
    elif age <= 70:
        price = 3200
    else:
        price = 3600
else: # 女性の場合
    if age <= 20:
        price = 2400
    elif age <= 50:
        price = 2400
    elif age <= 70:
        price = 2600
    else:
        price = 2800

print(f"料金は{price}円です。")

if gender == "M" and age <= 20:
    price = 2400
elif gender == "M" and age <= 50:
    price = 2800
elif gender == "M" and age <= 70:
    price = 3200
elif gender == "M" and age > 70:
    price = 3600
if gender == "F" and age <= 20:
    price = 2200
elif gender == "F" and age <= 50:
    price = 2400
elif gender == "F" and age <= 70:
    price = 2600
elif gender == "F" and age > 70:
    price = 2800

print(f"料金は{price}円です。")