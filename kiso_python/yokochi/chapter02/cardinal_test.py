while True:
    try:
        num = input("整数値:")
        int1 = int(num)
        print(int1 * 10)
        break
    except:
        print("整数値以外が入力されました。")