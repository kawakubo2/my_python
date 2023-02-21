name = "山田太郎"
age = 38

print("{}さんの年齢は{}歳です。".format(name, age))
print(f"{name}さんの年齢は{age}歳です")

print(name + "さんの年齢は" + str(age) + "歳です。")

radius = 5

import math

print("半径が{}cmの円の面積は{:.2f}平方cmです".format(radius, radius**2*math.pi))
print(f"半径が{radius}cmの円の面積は{radius**2*math.pi:.2f}平方cmです")

name1 = "山田"
name2 = "鈴木"

print("{1}さん！・・・{0}です。あれ？{1}さんですよね。".format(name2, name1))