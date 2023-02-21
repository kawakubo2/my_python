address = ["東京都大田区", "神奈川県三浦市", "千葉県銚子市", "東京都世田谷区", "神奈川県三浦市",
           "東京都文京区", "千葉県我孫子市", "神奈川県川崎市", "千葉県幕張市", "東京都渋谷区"]

pref = input("都道府県名: ")
if pref[-1]  in {"都", "道", "府", "県"}:
    cities = [a[len(pref):] for a in address if a.startswith(pref)]
    print(cities) 
else:
    print("最後に都、道、府、県をつけて入力してください")