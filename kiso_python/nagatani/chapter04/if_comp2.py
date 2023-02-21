import sys

address = ['東京都大田区', '神奈川県三浦市', '千葉県我孫子市', '東京都練馬区',
           '神奈川県川崎市', '東京都世田谷区', '千葉県銚子市', '神奈川県横浜市',
           '東京都渋谷区', '神奈川県川崎市']

pref = input('都道府県名: ')

if pref[-1] not in '都道府県':
    print('最後に都・道・府・県のいずれかを入力してください')
    sys.exit()

city = [a[len(pref):] for a in address if a.startswith(pref)]

print(city)