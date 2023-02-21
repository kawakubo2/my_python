# -*- coding: utf-8 -*-

weekday1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水', '木', '金', '土']
weekday3 = '日月火水木金土'

for en, ja in zip(weekday1, weekday2):
    print(en + ': ' + ja)
    
print('--------')

for en, ja in zip(weekday1, weekday3):
    print(en + ': ' + ja)