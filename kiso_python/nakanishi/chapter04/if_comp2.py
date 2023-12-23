import sys
addresses = ['東京都大田区', '神奈川県横須賀市', '千葉県我孫子市', '東京都世田谷区',
             '神奈川県逗子市', '千葉県幕張市', '東京都港区', '神奈川県川崎市']

prefs = {'都', '道', '府', '県'}
pref = input('都道府県名:(末尾は都・道・府・県を付けてください): ')
if pref[-1] not in prefs:
    print('末尾は都・道・府・県のいずれかを付けてください')
    sys.exit()

# addresses2 = [address[len(pref):] for address in addresses if address.startswith(pref)]
# print(addresses2)
addresses2 = [address[len(pref):] for address in addresses if address.startswith(pref)]
print(addresses2)