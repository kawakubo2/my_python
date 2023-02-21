# -*- coding: utf-8 -*-

year = int(input('年:'))
month = int(input('月:'))
date = int(input('日:'))

def print_date(year, month, date):
    print(str(year) + '年' + str(month) + '月' + str(date) + '日')
    print('{}年{}月{}日'.format(year, month, date))
    
print_date(year, month, date)