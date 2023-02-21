keyword = input("検索語: ")

members = ["山田太郎", "横山花子", "田中一郎", "山本久美子",
           "鈴木次郎", "星山裕子", "佐藤勝男"]

for member in members:
    if keyword not in member:
        continue
    print(member)