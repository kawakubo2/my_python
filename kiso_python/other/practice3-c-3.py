# -*- coding: utf-8 -*-

color1 = ['yellow', 'red', 'green']
color2 = ['黄色', '赤', '緑']

for en, ja in zip(color1, color2):
    print("{:10}:{}".format(en, ja))
