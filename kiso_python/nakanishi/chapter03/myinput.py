def input_int():
    while True:
        try:
            value = int(input("整数: "))
            break
        except ValueError:
            print("整数値を入力してください")
    return value
        
score = input_int()
if score >= 80:
    print("合格")
else:
    print("不合格")