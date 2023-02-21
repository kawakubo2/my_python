# -*- coding: utf-8 -*-

height = float(input('身長をcmで入力してください > '))

bmi = 22

# operator ・・・　演算子
# operand ・・・ 被演算子
std_weight = bmi * (height / 100) ** 2

print('身長: ' + str(height) + 'cm →　', end = '')
print('標準体重: ' + str(std_weight) + 'kg')

print('身長: {}cm → 標準体重: {:.2f}kg'.format(height, std_weight))