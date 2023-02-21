# -*- coding: utf-8 -*-

# trapezoid・・・台形

upper_base = float(input("上底を入力してください: "))
lower_base = float(input("下底を入力してください: "))
height     = float(input("高さを入力してください: "))

area = (upper_base + lower_base) * height / 2

print("上底が" + str(upper_base) + "cm", end="")
print("下底が" + str(lower_base) + "cm", end="")
print("高さが" + str(height) + "cm", end="")
print("の台形の面積は" + str(area) + "平方cmです")

str1 = "私は今日、\nPythonを勉強しました\t"
print(str1)