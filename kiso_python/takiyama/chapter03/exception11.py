while True:
    try:
        score = int(input("点数(0-100): "))
        if 0 <= score <= 100:
            break
        else:
            print("点数は0～100の間を入力してください")
    except ValueError:
        print("点数は整数値を入力してください")
    
if score >= 80:
    print("合格です")
else:
    print("不合格です")