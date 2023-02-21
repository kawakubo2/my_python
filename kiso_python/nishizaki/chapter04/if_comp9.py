names1 = ["山田太郎", "横山花子", "田中一郎", "山本久美子", "鈴木次郎", "星山裕子", "佐藤勝男"]

keyword = input("文字を入力してください: ")
names2 = [name for name in names1 if keyword in name]
print(names2)