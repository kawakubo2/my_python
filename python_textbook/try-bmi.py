# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:09:01 2017

@author: tomoharu
"""
while True:
    try:
        weight = float(input("体重(kg): "))
        break
    except ValueError:
        print("数値ではない値を検出")
while True:
    try:
        height = float(input("身長(cm): "))
        bmi = weight / ((height / 100) * (height / 100))
        break
    except ValueError:
        print("数値でない値を検出")
    except ZeroDivisionError:
        print("身長に0は指定できません")

result = ""

if bmi < 18.5:
    result = "やせ気味"
elif bmi < 25:
    result = "標準体重"
elif bmi < 30:
    result = "肥満(軽)"
else:
    result = "肥満(重)"

print("BMI:", bmi)
print("判定:", result)