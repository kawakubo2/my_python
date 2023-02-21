# -*- coding: utf-8 -*-

members = [
    {'name': '山田太郎', 'age': 25, 'height': 172, 'weight': 78},
    {'name': '横山花子', 'age': 32, 'height': 165, 'weight': 55},
    {'name': '田中一郎', 'age': 42, 'height': 178, 'weight': 82},
    {'name': '山本久美子', 'age': 38, 'height': 155, 'weight': 48},
]

def bmi(weight, height):
    return weight / (height / 100) ** 2

for member in members:
    print("名前:{}, 年齢:{} 身長:{} 体重:{} BMI:{}".format(member['name']\
          ,member['age'], member['height'], member['weight'],\
          bmi(member['weight'], member['height'])
          ))
    
