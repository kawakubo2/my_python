try:
    score = int(input('点数を入力してください: '))
    print('入力した点数:', score)
    if score >= 80:
        print('合格')
    else:
        print('不合格')
except:
    print('整数を入力してください')