while True:
    try:
        score = int(input("点数(0-100): "))
        if 0 <= score <= 100:
            break
        else:
            print("0から100までの整数値を入力してください")
    except ValueError:
        print("整数を入力してください")

if score >= 80:
    print("合格")
else:
    print("不合格")