# -*- coding: utf-8 -*-

colors_en = ['yellow', 'red', 'green']
colors_ja = ['黄色', '赤', '緑']

for en, ja in zip(colors_en, colors_ja):
    print("{:6s}:{}".format(en, ja))