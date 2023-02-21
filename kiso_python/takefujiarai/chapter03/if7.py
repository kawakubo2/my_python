# -*- coding: utf-8 -*-

num = int(input('数値を入力してください: '))

if (num % 3 == 0 or num % 5 == 0) and num >= 100:
    print('100以上の3または5の倍数です。')