# -*- coding: utf-8 -*-

dansu = int(input('ピラミッドの段数:'))

for i in range(dansu):
    print(' ' * (dansu - i), end='')
    print('*' * (i * 2 + 1), end='')
    print('')