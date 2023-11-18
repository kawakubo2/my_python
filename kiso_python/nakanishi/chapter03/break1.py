words = ["旅行", "桜", "テレビ", "終了", "岸辺", "ラジオ"]

for word in words:
    if word == "終了":
        print("ループを中断しました。")
        break
    print(word)

members = ["tiger", "apple", "tomato", "math", "james", "john", "summer", "grape"]
username = "john"
for m in members:
    if m == "john":
        print(f"{username}は存在します。別のユーザ名を入力してください。")
        break
