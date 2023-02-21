# -*- coding: utf-8 -*-

# month = int(input('月の値を入力してください: '))

for month in range(14): 
    print(str(month) + ':', end='')
    if month == 12 or month == 1 or month == 2:
        print('冬')
    elif 3 <= month <= 5:
        print('春')
    elif 6 <= month <= 8:
        print('夏')
    elif 9 <= month <= 11:
        print('秋')
    else:
        print('1～12の値を入力してください')
        
def month2season(month):
    if month in (12, 1, 2):
        season = '冬'
    elif month in (3, 4, 5):
        season = '春'
    elif month in (6, 7, 8):
        season = '夏'
    elif month in (9, 10, 11):
        season = '秋'
    else:
        season = '1～12の値を入力してください'
        
    return season

print('---関数版テスト---')
for n in range(14):
    print(str(n) + ':', end='')
    print(month2season(n))
