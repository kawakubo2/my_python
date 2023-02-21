try:
    score = int(input("点数: "))
    if score >= 80:
        print("合格です")
    else:
        print("不合格です")
except ValueError:
    print("整数を入力してください")
