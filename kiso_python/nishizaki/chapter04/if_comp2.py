address = ["東京都千代田区", "千葉県船橋市", "東京都杉並区", "埼玉県大宮市",
           "東京都町田市", "東京都西東京市", "東京都大田区", "神奈川県横浜市",
           "神奈川県逗子市", "千葉県銚子市", "東京都品川区"]

pref = input("都道府県名を入力してください: ")
if pref[-1] in ("都", "道", "府", "県"):
    # towns = [town[len(pref):] for town in address if town.startswith(pref)]
    towns = [town.removeprefix(pref) for town in address if town.startswith(pref)]
    print(towns)
else:
    print("都道府県名の指定に誤りがあります。")