words = ['旅行', '桜', 'テレビ', '岸辺', 'ラジオ']

for word in words:
    if word == '終了':
        print('***ループを中断しました***')
        break
    print(word)
else:
    print('***ループが完了しました***')
    
    
members = ['山田太郎', '横山花子', '田中一郎', '鈴木次郎']

for member in members:
    if member == '田中一郎':
        print('田中一郎さんは名簿に存在します')
        break
else:
    print('田中一郎さんは名簿には存在しません')
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
for n in numbers:
    try:
        total += n
    except:
        break
else:
    print('合計：', total)



    
