
while True:
    try:
        num = int(input("整数: "))
        break
    except:
        print("整数の形式に誤りがあります")

print(num)