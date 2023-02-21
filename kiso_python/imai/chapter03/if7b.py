# -*- coding: utf-8 -*-

"""
0  - 11 　---> おはようございます
12     　---> お昼です
13 - 18 ---> こんにちは
19 - 23 ---> こんばんは

上記の値は境界値となりすべてテスト---> 境界値テスト
範囲内の値は任意の値を選び出しテスト ---> 同値テスト

"""


def greeting(time):
    print('---{}時です---'.format(time))
    if time < 0 or time > 23:
        print('時刻の範囲を超えています。')
    elif time <= 11:
        print('おはようございます')
    elif time == 12:
        print('お昼です')
    elif time <= 18:
        print('こんにちは')
    else:
        print('こんばんは')
        
    if time < 0 or time > 23:
        print('時刻の範囲を超えています。')
    elif time > 18:
        print('こんばんは')
    elif time > 12:
        print('こんにちは')
    elif time == 12:
        print('お昼です')
    else:
        print('おはようございます')
        
for t in range(-1, 25):
    greeting(t)