# -*- coding: utf-8 -*-

height = float(input('身長(cm)を入力してください: '))

bmi = 22

"""
bmi = 体重 / 身長の2乗
体重 = 22 * 身長の2乗
"""

std_weight = bmi * (height / 100) ** 2
print('身長: ' + str(height) + 'cm → ', end='')
# print('標準体重: ' + str(std_weight) + 'kg')
print('標準体重: {:.1f}kg'.format(std_weight))