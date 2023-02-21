# -*- coding: utf-8 -*-

words = ['空', '秘密', 'ひらけごま', '海', 'ギター']

str = input('文字列を入力してください: ')

try:
    index = words.index(str)
    print('{}のインデックスは{}です。'.format(str, index))
except ValueError:
    print('{}は見つかりませんでした。'.format(str))