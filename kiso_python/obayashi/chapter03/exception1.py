import sys
try:
    score = int(input("点数を入力してください: "))
    if score >= 80:
        print("合格です")
    else:
        print("不合格")
except ValueError:
    print("数値を入力してください")
    sys.exit()
