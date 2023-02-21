# -*- coding: utf-8 -*-

customers = [
    {'name': '田中一郎', 'height': 168, 'weight': 72},
    {'name': '横山花子', 'height': 165, 'weight': 58},
    {'name': '山田太郎', 'height': 170, 'weight': 68},
    {'name': '星山裕子', 'height': 158, 'weight': 52},
    {'name': '佐藤勝男', 'height': 172, 'weight': 76},
    {'name': '鈴木次郎', 'height': 180, 'weight': 80},
]

def bmi(weight, height):
    return weight / (height/100) ** 2

for c in sorted(customers, key=lambda c: bmi(c['weight'], c['height'])):
    print(c, "{:.2f}".format(c['weight'] / (c['height'] / 100) ** 2))