# -*- coding: utf-8 -*-

address = ['東京都千代田区', '神奈川県鎌倉市', '東京都大田区', '千葉県幕張市', '東京都三鷹市', '神奈川県川崎市',
           '千葉県我孫子市', '東京都町田市', '神奈川県横須賀市', '東京都世田谷区']

pref = input('都道府県名を入力してください: ')
city = [town[len(pref):] for town in address if town.startswith(pref)]
print(city)