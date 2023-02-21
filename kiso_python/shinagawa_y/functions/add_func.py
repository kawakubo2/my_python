# -*- coding: utf-8 -*-

def input_positive_number(prompt):
    """
    この関数は正の整数を入力するためのもの
    正しく入力するまで続ける
    """
    while(True):
        try:
            result = int(input(prompt + ' : '))
            if result > 0:
                return result
        except:
            print('正の整数を入力してください')


def input_dansu():
    """
    この関数は正の整数を入力するためのもの
    正しく入力するまで続ける
    """
    while(True):
        try:
            dansu = int(input('ピラミッドの段数を入力してください : '))
            if dansu > 0:
                return dansu
        except:
            print('段数は正の整数を入力してください')

def input_step():
    while(True):
        try:
            step = int(input('1段ごとに増える石の数(1～5) : '))
            if 1 <= step <= 5:
                return step
        except:
            print('段数は正の整数を入力してください')


d = input_dansu()
s = input_step()

for i in range(d):
    print('-' * ((d - 1 - i) * s), end='')
    print('*' * ((i * 2) * s + 1), end='')
    print('-' * ((d - 1 - i) * s))