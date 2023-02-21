
while True:
    try:
        score = int(input('点数: '))
        if 0 <= score <= 100:
            break
    except ValueError:
        print('整数値を入力してください')
    # score = int(input('点数(0-100): '))
    # if 0 <= score <= 100:
    #     break
    # else:
    #     print('点数は0～100の範囲で入力してください')