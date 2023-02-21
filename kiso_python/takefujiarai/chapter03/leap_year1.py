# -*- coding: utf-8 -*-

year = int(input('年の値を入力してください: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('閏年です。')
else:
    print('閏年ではありません')