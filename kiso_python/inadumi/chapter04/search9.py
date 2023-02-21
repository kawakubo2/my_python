# -*- coding: utf-8 -*-

keyword = input('検索文字列: ')
with open('search1.py', 'r', encoding='utf_8') as f:
    linenum = 1
    for line in f:
        if keyword in line:
            print('{}:{}'.format(linenum, line.rstrip('\n')))
        linenum += 1
            