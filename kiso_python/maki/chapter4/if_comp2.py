# -*- coding: utf-8 -*-

import sys

address = ['東京都大田区', '神奈川県川崎市', '東京都東村山市', '神奈川県横浜市',
           '千葉県幕張子', '千葉県銚子市', '東京都文京区', '神奈川県逗子市']

pref = input('都道府県名を入力してください: (例: 千葉県) : ')

if pref[-1:] not in ['都', '道', '府', '県']:
    print('最後は都道府県の文字を入れてください')
    sys.exit(-1)

cities = [city[len(pref):] for city in address if city.startswith(pref)]

print(cities)