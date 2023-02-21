while True:
    try:
        score = int(input("点数を入力してください: "))
        if 0 <= score <= 100:
            break
        else:
            print("0～100の値を入力してください")
            continue
    except ValueError:
        print("数値を入力してください")
    
if score >= 80:
    print("合格です")
else:
    print("不合格です")