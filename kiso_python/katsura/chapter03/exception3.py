try:
    score = int(input('点数: '))
except:
    print("数値を入力してください")
else:
    print("入力した値:", score)
    if score >= 80:
        print("合格")
    else:
        print("不合格")

try:
    score = int(input('点数: '))
    print("入力した値:", score)
    if score >= 80:
        print("合格")
    else:
        print("不合格")
except:
    print("数値を入力してください")