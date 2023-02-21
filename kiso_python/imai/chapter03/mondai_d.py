# -*- coding: utf-8 

import input_util

age = input_util.input_not_negative('年齢を入力してください : ')

if age >= 13:
    print('大人料金です')
else:
    print('子供料金です')