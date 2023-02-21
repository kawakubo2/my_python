# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:48:30 2017

@author: tomok
"""

weekday1 = ['Sun', 'Mon', 'Tue', 'Wed',
            'Thu', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水',
            '木', '金', '土']
for english, japanese in zip(weekday1, weekday2):
    print(english + ':' + japanese)
