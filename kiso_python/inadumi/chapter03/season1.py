# -*- coding: utf-8 -*-
  
def get_season_name(month):
    result = ''
    if month == 12 or month == 1 or month == 2:
        result = '冬'
    elif month >= 3 and month <= 5:
        result = '春'
    elif month >= 6 and month <= 8:
        result = '夏'
    elif month >= 9 and month <= 11:
        result = '秋'
    else:
        result = '1～12の値を入力してください'
        
    return result

counter = 0
season_dict = {1:'冬', 2:'冬', 3:'春', 4:'春', 5:'春', 6:'夏', 7:'夏', 8:'夏', 9:'秋', 10:'秋', 11:'秋', 12:'冬'}
for season in season_dict.items():
    if get_season_name(season[0]) == season[1]:
        counter += 1
    print('月:{:2d} 季節:{} 判定:{}'.\
          format(season[0], get_season_name(season[0]),\
          '○' if get_season_name(season[0]) == season[1] else '×'))

print('{}/{} '.format(counter, len(season_dict)), end='')
print('合格' if len(season_dict) == counter else '不合格')