import sys

addresses = ['東京都大田区', '東京都世田谷区', '神奈川県逗子市', '千葉県幕張市',
             '神奈川県三崎市', '千葉県銚子市', '東京都台東区', '埼玉県熊谷市',
             '神奈川県鎌倉市']

pref = input('都道府県名を入力してください: ')

if pref[-1] not in {'都', '道', '府', '県'}:
    print('都・道・府・県を末尾に付けて入力してください')
    sys.exit(-1)
cities = [city[len(pref):] for city in addresses if city.startswith(pref)]
print(cities)