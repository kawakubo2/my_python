# -*- coding: utf-8 -*-

month = int(input('月の値を入力してください : '))

if month == 12 or month == 1 or month == 2:
    print('冬')
elif 3 <= month <= 5:
    print('春')
elif 6 <= month <= 8:
    print('夏')
elif 9 <= month <= 11:
    print('秋')
else:
    print('1~12の値を入力してください')