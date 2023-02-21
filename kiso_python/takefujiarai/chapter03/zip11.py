# -*- coding: utf-8 -*-

weekday_en = ['Sun', 'Mon','Tue','Wed','Thu','Fri','Sat']
weekday_ja = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(weekday_en, weekday_ja):
    print("{}:{}".format(en, ja))