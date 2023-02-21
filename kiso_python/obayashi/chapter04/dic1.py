dic = {"日": "Sun", "月": "Mon", "火": "Tue", "水": "Wed", "木": "Thu", "金": "Fri", "土": "Sat"}

while True:
    key = input("キーを入力してください(終了の場合 q): ")
    if key == "q": break
    if key in dic:
        print(dic[key])
    else:
        print(key + "は辞書に存在しません")
