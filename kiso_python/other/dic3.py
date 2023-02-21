# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:17:55 2017

@author: tomok
"""

dic = {"日": "Sun", "月": "Mon", "火": "Tue",
 "水": "Wed", "木": "Thu", "金": "Fri", "土": "Sat"}
 
key = input("キーを入力してください ")
if key in dic:
    del dic[key]
    print(dic)
else:
    print('キー"{}"が見つかりませんでした'.format(key))
