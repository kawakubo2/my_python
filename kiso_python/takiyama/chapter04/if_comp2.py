import sys

addresses = ["東京都大田区", "神奈川県小田原市", "千葉県銚子市", "東京都世田谷区",
             "神奈川県逗子市", "千葉県我孫子市", "東京都葛飾区", "千葉県市川市",
             "東京都渋谷区", "神奈川県三浦市", "千葉県船橋市"]

pref = input("都道府県名: ")
if pref[-1] not in ["都","道","府","県"]:
    print("末尾に都、道、府、県を付けて入力してください")
    sys.exit()

cities = [address[len(pref):] for address in addresses if address.startswith(pref)]
if len(cities) > 0:
    print(cities)
else:
    print("該当なし")