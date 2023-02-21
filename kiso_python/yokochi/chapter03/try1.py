while True:
    try:
        score = int(input('点数(0-100): '))
        if score < 0 or score > 100:
            print('0～100の間の数値を入力してください。')
            continue
        break
    except:
        print('整数値を入力してください')

if score >= 80:
    print('合格です。')
else:
    print('不合格です')