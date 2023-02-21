age = int(input('年齢を入力してください: '))

if age < 0:
    print('年齢は0以上を入力してください')
elif age < 3:
    print('無料です')
elif age < 13:
    print('200円です')
elif age < 65:
    print('400円です')
else:
    print('無料です')