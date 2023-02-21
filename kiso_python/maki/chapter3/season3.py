# -*- coding: utf-8 -*-

# month = int(input('月の値を入力してください : '))

def get_season_by_month(month):
    season = ''
    if month in (12, 1, 2):
        season = '冬'
    elif month in (3, 4, 5):
        season = '春'
    elif month in (6, 7, 8):
        season = '夏'
    elif month in (9, 10, 11):
        season = '秋'
    else:
        season = '1~12の値を入力してください'
    return season
        
for m in range(14):
    print(str(m) + '月' + get_season_by_month(m) + 'です。')