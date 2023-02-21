names = ['山田太郎', '横山花子', '田中一郎', '山本久美子', '鈴木次郎', '星山裕子', '佐藤勝男']

keyword = input('キーワード: ')

for name in names:
    if keyword in name:
        print(name)
