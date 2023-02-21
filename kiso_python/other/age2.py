# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:10:21 2017

@author: tomok
"""
age = int(input('年齢を入力してください: '))

msg = '未成年' if age < 20 else '成人'
print(msg)

if age < 20:
    print('未成年')
else:
    print('成人')


