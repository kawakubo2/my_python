# -*- coding: utf-8 -*-

# pyramid.py

dansu = int(input('ピラミッドの段数を入力してください : '))

for i in range(dansu):
    print(' ' * (dansu - 1 - i), end='')
    print('*' * (i * 2 + 1))
    
    

    
