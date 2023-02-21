# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:03:48 2017

@author: tomok
"""

age = int(input('年齢を入力してください: '))

if (age == 3) or (age == 5) or (age == 7):
    print('七五三です')

if age == 3 or age == 5 or age == 7:
    print('七五三です')

gender = int(input('性別を入力してください 1:男性 2:女性 '))
if (age == 20 or age == 30) and gender == 2:
    print('半額クーポンを差し上げます')