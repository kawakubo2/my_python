# -*- coding: utf-8 -*-

year = int(input('生まれた年を入力してください: '))

if year >= 2019:
    print('令和生まれですね')
elif year >= 1989:
    print('平成生まれですね')
else:
    print('う？昭和')