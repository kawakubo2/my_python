def get_english_season(ja_season):
    if ja_season not in ["春", "夏", "秋", "冬"]:
        raise ValueError("季節名に誤りがあります")
    if ja_season == "春":
        en_season = "Spring"
    elif ja_season == "夏":
        en_season = "Summer"
    elif ja_season == "秋":
        en_season = "Autumn"
    else:
        en_season = "Winter"
    return en_season

def get_english_season2(ja_season):
    seasons = {"春": "Spring", "初夏": "Early Summer", "夏": "Summer", "秋": "Autumn", "晩秋": "Late Autumn", "冬": "Winter"}
    if ja_season not in seasons:
        raise ValueError("季節名に誤りがあります")
    return seasons[ja_season]

s = input("日本語の季節名: ")
try:
    print(f"{s}は英語で{get_english_season2(s)}")
except ValueError as e:
    print(e)

employees = {
        1001: {"氏名": "山田太郎", "年齢": 38, "住所": "東区箱崎"},
        1002: {"氏名": "横山花子", "年齢": 43, "住所": "東区南区"},
        1003: {"氏名": "田中一郎", "年齢": 52, "住所": "太宰府"},
}


employees[1001]["住所"] = "日田"
employees[1004] = {"氏名": "山本久美子", "年齢": 33, "住所": "久留米"}
for number, info in employees.items():
    print(f'氏名: {info["氏名"]}')
    print(f'年齢: {info["年齢"]}')
    print(f'住所: {info["住所"]}')


colors = {"青": "blue", "赤": "red", "黒": "black", "白": "white"}

color = input("色: ")
if color in colors:
    print(f"{color}は英語で{colors[color]}")
else:
    print(f"申し訳ありません。辞書には{color}はありません。")

employees = {"田中": 35, "鈴木": 28, "遠藤": 31, "佐々木": 22}

fruits = {"バナナ": 3, "リンゴ": 2.5, "イチゴ": 10}
for key in fruits.keys():
    print(key)
for val in fruits.values():
    print(val)
print("===< 今日の売り上げ >===")
for fruit_name, num in fruits.items():
    print(f"{fruit_name}: {num}万円")

for key in fruits.keys():
    print(fruits[key])

fruits2 = ["バナナ", "リンゴ", "イチゴ", "バナナ", "バナナ", "イチゴ", "ブドウ"]

fruit_counter = {}
for fruit in fruits2:
    if fruit in fruit_counter:
        fruit_counter[fruit] += 1
    else:
        fruit_counter[fruit] = 1

# {"バナナ": 3, "リンゴ": 1, "イチゴ": 2, "ブドウ": 1}
    
for fruit, num in fruit_counter.items():
    print(f"{fruit}: {num}個")
    