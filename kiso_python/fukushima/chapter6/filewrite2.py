# -*- coding: utf-8 -*-

with open('out.txt', 'w', encoding='utf_8') as f:
    f.writelines([w + '曜日\n' for w in '日月火水木金土'])