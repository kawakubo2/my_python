# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 22:13:36 2017

@author: tomok
"""

age = int(input('年齢を入力してください: '))
if age < 3:
    print('無料です')
elif age < 13:
    print('200円です')
elif age < 65:
    print('400円です')
else:
    print('無料です')

print('------')

if age >= 65:
    print('無料です')
elif age >= 13:
    print('400円です')
elif age >= 3:
    print('200円です')
else:
    print('無料です')