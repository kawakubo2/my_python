addresses = ['東京都大田区', '神奈川県横浜市', '千葉県幕張子', '千葉県銚子市', '東京都世田谷区',
            '神奈川県横須賀市', '埼玉県大宮市', '東京都文京区']

pref = input('都道府県名: ')

if pref[-1] in '都道府県':
    cities = [ address[len(pref):] for address in addresses if address.startswith(pref)]
    print(cities)
else:
    print('都道府県名の指定に誤りがあります。')