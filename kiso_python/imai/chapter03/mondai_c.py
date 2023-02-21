# -*- coding: utf-8 -*-

colors1 = ['yellow', 'red', 'green']
colors2 = ['黄色', '赤', '緑']

for e, j in zip(colors1, colors2):
    print('{:8s} : {}'.format(e, j))