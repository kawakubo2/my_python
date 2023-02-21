# -*- coding: utf-8 -*-

# age = int(input('年齢を入力してください:'))

def calc_price(age):
    result = ''
    if age < 3:
        result = '無料です'
    elif age < 13:
        result = '200円です'
    elif age < 65:
        result = '400円です'
    else:
        result = '無料です'
    return result
        
ages_ok = {0: '無料です', 1: '無料です', 2: '無料です', 3: '200円です', 8: '200円です', 12: '200円です', 13: '400円です', 38: '400円です', 64: '400円です', 65: '無料です'}

for age in ages_ok.items(): # age ---> (0, '無料')
    print('------')
    print('検出値:{} 期待値:{} 結果:{}'.format(calc_price(age[0]), age[1], '○' if calc_price(age[0]) == age[1] else '×'))
    

    