# -*- coding: utf-8 -*-

time = int(input('時刻を入力してください : '))

if time < 0 or time > 23:
    print("範囲外です")
elif time <= 11:
    print("おはようございます")
elif time == 12:
    print("お昼です")
elif time <= 18:
    print("こんにちは")
else:
    print("こんばんは")
    
if 0 <= time <= 11:
    print("おはようございます")
elif time == 12:
    print("お昼です")
elif 13 <= time <= 18:
    print("こんにちは")
elif 19 <= time <= 23:
    print("こんばんは")
else:
    print("範囲外です")
    
if time < 0 or time > 23:
    print("範囲外")
elif time >= 19:
    print("こんばんは")
elif time >= 13:
    print("こんにちは")
elif time == 12:
    print("お昼です")
else:
    print("おはようございます")
    
age = int(input("年齢を入力してください : "))

sex = int(input("性別を入力してください 1:女性 2:男性 : "))

if sex == 1:
    if age <= 20:
        print("2000円です")
    elif age <= 50:
        print("2200円です")
    elif age <= 70:
        print("2400円です")
    else:
        print("2600円です")
else:
    if age <= 20:
        print("2400円です")
    elif age <= 50:
        print("2800円です")
    elif age <= 70:
        print("3200円です")
    else:
        print("3600円です")
        
if sex == 1 and age <= 20:
    print("2000円です")