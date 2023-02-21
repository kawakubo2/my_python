# -*- coding: utf-8 -*-

weekday1 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
weekday2 = ['月', '火', '水', '木', '金', '土', '日']

for en, ja in zip(weekday1, weekday2):
    print(en + ':' + ja)