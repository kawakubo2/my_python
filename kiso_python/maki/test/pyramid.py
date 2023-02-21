# -*- coding: utf-8 -*-

dansu = int(input('段数を入力してください : '))

for i in range(dansu):
    print(' ' * (dansu - 1 - i) , end='')
    print('*' * (i * 2 + 1))
    