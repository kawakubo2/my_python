while True:
    score = int(input("点数を入力してください: "))
    if 0 <= score <= 100:
        break
    else:
        print("0～100の値を入力してください")
        