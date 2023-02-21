# -*- coding: utf-8 -*-

# month = int(input('月の値を入力してください : '))

def get_season(month):
    
    if month in (12, 1, 2):
        season = '冬'
    elif month in (3, 4, 5):
        season = '春'
    elif month in (6, 7, 8):
        season = '夏'
    elif month in (9, 10, 11):
        season = '秋'
    else:
        return False
    return season
        
for m in range(0, 14):
    s = get_season(m)
    if s:
        print("{}月は{}です。".format(m, s))
    else:
        print("1～12の値を入力してください")
