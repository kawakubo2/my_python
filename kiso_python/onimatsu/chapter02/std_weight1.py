# -*- coding: utf-8 -*-

height = float(input('身長をcm単位で入力してください: '))
bmi = 22
std_weight = bmi * (height / 100) ** 2
print("身長:" + str(height) + "cm → ", end="")
print("標準体重:" + str(std_weight) + "kg")

passwd = "81dc9bdb52d04dc20036dbd8313ed055"
print(len(passwd))