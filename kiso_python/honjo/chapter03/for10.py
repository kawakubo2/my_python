# -*- coding: utf-8 -*-

DANSU = int(input('ピラミッドの段数を入力してください :'))

for n in range(1, DANSU + 1):
    print(' ' * (DANSU - n), end='')
    print('*' * (n * 2 - 1), end= '')
    print(' ' * (DANSU - n), end='')
    print('')