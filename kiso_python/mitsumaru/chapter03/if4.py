age = int(input('年齢を入力してください: '))

if age < 3:
    print('無料です')
elif age < 13:
    print('200円')
elif age < 65:
    print('400円')
else:
    print('無料です')
    