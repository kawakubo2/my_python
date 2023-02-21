# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:41:47 2017

@author: tomok
"""

day_of_week_en = {'Sun': '日', 'Mon': '月', 'Tue': '火', 'Wed': '水', 'Thu': '木','Fri': '金', 'Sat': '土'}
print(day_of_week_en)

day_of_week_ja = {}
for en, ja in day_of_week_en.items():
    day_of_week_ja[ja] = en

print(day_of_week_ja)