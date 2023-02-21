# -*- coding: utf-8 -*-

addresses = ['東京都大田区', '神奈川県川崎市', '千葉県銚子市', '東京都世田谷区', '神奈川県三崎市',
           '千葉県幕張市', '東京都板橋区', '神奈川県逗子市', '千葉県我孫子市', '東京都北区']

pref = input('都道府県名を入力してください: ')

if pref[-1:] in {'都', '道', '府', '県'}:
    cities = [address[len(pref):] for address in addresses if address.startswith(pref)]
    print(cities)
else:
    print('都・道・府・県を末尾に付けて入力してください')