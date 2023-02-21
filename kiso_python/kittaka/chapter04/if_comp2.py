import sys

addresses = ["東京都大田区", "神奈川県逗子市", "千葉県銚子市", "東京都練馬区",
             "神奈川県三浦市", "千葉県幕張子", "神奈川県小田原市", "東京都世田谷区",
             "千葉県八千代市", "神奈川県川崎市"]

pref = input("都道府県名: ")
if pref[-1] not in "都道府県":
    print("最後に都・道・府・県をつけてください")
    sys.exit()

pref_address = [address[len(pref):] for address in addresses if address.startswith(pref)]
print(pref_address)