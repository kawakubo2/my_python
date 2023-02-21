# -*- coding: utf-8 -*-

year = int(input('生まれた年を入力してください : '))
month = int(input('生まれた月を入力してください : '))

if (year, month) >= (2019, 6):
    print('令和生まれですね')
elif (year, month) >= (1989, 1):
    print('平成生まれですね')
else:
    print('昭和以前の生まれですね')
    
    
if year > 2019 or year == 2019 and month > 5:
    print('令和')
elif year >= 1989 and month >= 1:
    print('平成')
else:
    print('昭和以前')
    
    

