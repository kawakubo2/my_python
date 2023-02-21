# -*- coding: utf-8 -*-

colors1 = ['yellow', 'red', 'green', 'aquamarine']
colors2 = ['黄色', '赤', '緑', '海色']

max_length = max([len(c) for c in colors1])

format_str = '{:' + str(max_length) + 's}:{}'

for en, ja in zip(colors1, colors2):
    print(format_str.format(en, ja))