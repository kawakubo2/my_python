# -*- coding: utf-8 -*-

address = ["東京都千代田区", "千葉県船橋市", "千葉県幕張市"
           , "千葉県我孫子市", "神奈川県横浜市", "神奈川県川崎市"
           , "東京都大田区", "神奈川県鎌倉市", "東京都町田市"]

city = input("都道府県名を入力してください : ")

pref_cities = \
    [town[len(city):] for town in address if town.startswith(city)]

print(pref_cities)