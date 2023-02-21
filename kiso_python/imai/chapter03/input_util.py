# -*- coding: utf-8 -*-

def input_range(min, max, prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('整数値を入力してください')
            continue
        if min <= num <= max:
            break
    return num

def input_not_negative(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('整数値を入力してください')
            continue
        if num >= 0:
            break;
    return num
            

