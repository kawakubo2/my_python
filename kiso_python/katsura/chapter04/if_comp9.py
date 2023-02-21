import sys
address = ["東京都千代田区", "千葉県船橋市", "東京都杉並区", "埼玉県大宮市",
 "東京都西東京市", "東京都町田市", "東京都大田区", "神奈川県横浜市"]

pref = input('都道府県を入力してください')
if pref[-1] not in '都道府県':
    print('最後に都・道・府・県をつけてください')
    sys.exit()

towns = [town[len(pref):] for town in address if town.startswith(pref)]
print(towns)