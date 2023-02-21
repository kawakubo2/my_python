addresses = ["東京都大田区", "神奈川県相模原市", "千葉県我孫子市", "東京都世田谷区",
             "神奈川県横須賀市", "東京都台東区", "千葉県幕張子", "神奈川県三浦市"]

pref = input("都道府県名を入力してください: ")
if pref[-1] in ("都", "道", "府", "県"):
    cities = [address[len(pref):] for address in addresses if address.startswith(pref)]
    print(cities)
else:
    print(f"{pref}に該当する市区町村が見つかりませんでした")
    print("末尾には必ず都、道、府、県をつけてください")