# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:35:52 2017

@author: tomok
"""

countries = ['フランス', 'アメリカ', '中国', 'ドイツ', '日本']

cnt = 0
for country in countries:
    print(str(cnt + 1) + ":" + country)
    cnt += 1
