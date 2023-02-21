# -*- coding: utf-8 -*-

def input_positive_int(prompt):
    while True:
        try:
            result = int(input(prompt + 'を入力してください : '))
        except ValueError:
            print('整数を入力してください。')
            continue
        if result <= 0:
            print('正数を入力してください。')
        else:
            return result