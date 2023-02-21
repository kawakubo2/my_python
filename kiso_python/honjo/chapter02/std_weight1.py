# -*- coding: utf-8 -*-

"""
BMI = 体重(kg) / (身長(m)の2乗)
BM*身長の2乗 = 体重
"""

height = float(input("身長(cm)を入力してください: "))

bmi = 22
std_weight=bmi*(height/100)**2
print("身長: " + str(height) + "cm -> ", end="")
print("標準体重: " + str(std_weight) + "kg")

