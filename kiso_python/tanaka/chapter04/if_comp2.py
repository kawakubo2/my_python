addresses = ['東京都大田区', '神奈川県逗子市', '千葉県我孫子市', '東京都板橋区',
             '神奈川県三浦市', '千葉県幕張子', '東京都品川区', '神奈川県横須賀市',
             '東京都文京区', '千葉県銚子市', '東京都北区']

pref_name = input("都道府県名(末尾は都道府県をつけてください): ")
if pref_name[-1] in ('都', '道', '府', '県'):
    pref_address = [address.removeprefix(pref_name) for address in addresses if address.startswith(pref_name)]
    print(pref_address)
else:
    print("末尾に都、道、府、県をつけてください。")