# -*- coding: utf-8 -*-
import sys

pref = input('都道府県名を入力してください: ')

if pref[-1] not in {'都', '道', '府', '県' }:
    print('最後に都・道・府・県のいずれかを付加して入力してください')
    sys.exit(-1)
    
address = ['東京都大田区', '神奈川県横浜市', '東京都葛飾区', '神奈川県鎌倉市',
           '東京都練馬区', '千葉県幕張市', '神奈川県逗子市', '東京都世田谷区',
           '千葉県我孫子市']

cities = [town[len(pref):] for town in address if town.startswith(pref)]

print(cities)
    
    
    