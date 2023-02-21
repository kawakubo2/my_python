# -*- coding: utf-8 -*-
"""
Created on Fri May  5 20:20:16 2017

@author: tomok
"""

words = ['空', '秘密', '電柱', 'ひらけごま', '海', 'ギター']

str = input('文字列を入力してください: ')

try:
    index = words.index(str)
    print("{}のインデクスは{}です".format(str, index))
except ValueError:
    print("{}は見つかりませんでした".format(str))