import sys

addresses = ['東京都大田区', '神奈川県三浦市', '千葉県我孫子市', '東京都練馬区',
           '神奈川県横浜市', '千葉県幕張子', '東京都世田谷区', '千葉県銚子市',
           '神奈川県鎌倉市', '東京都港区']

pref = input('都道府県名を入力してください: ')
if pref[-1] not in '都道府県':
    print('都・道・府・県を最後につけて入力してください')
    sys.exit()

city = [address[len(pref):] for address in addresses if address.startswith(pref)]
# city = [address.removeprefix(pref) for address in addresses if address.startswith(pref)]
print(city)
