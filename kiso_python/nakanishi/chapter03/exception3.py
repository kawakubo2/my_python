try:
    score = int(input("点数: "))
except:
    print("整数値を入力してください")
else:
    print("入力した点数:", score)
    if score >= 80:
        print("合格")
    else:
        print("不合格")