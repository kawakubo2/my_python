# -*- coding: utf-8 -*-

weekdays = ['日','月','火', '水', '木', '金', '土']

with open('days.txt', 'w', encoding='utf_8') as f:
    f.writelines([w + '曜日\n' for w in weekdays])