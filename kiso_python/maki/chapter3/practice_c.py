# -*- coding: utf-8 -*-

colors1 = ['yellow', 'red', 'green']
colors2 = ['黄色', '赤', '緑']

for en_color, ja_color in zip(colors1, colors2):
    print("{:6s}: {}".format(en_color, ja_color))