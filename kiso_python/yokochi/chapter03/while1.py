# while文

while True:
    try:
        score = int(input('点数を入力してください: '))
        if score < 0 or score > 100:
            print('0～100の数値を入力してください')
            continue
        break
    except:
        print('整数値を入力してください')