age = int(input("年齢を入力してください: "))
print("未成年" if age < 20 else "成人")

if age < 20:
    msg = "未成年"
else:
    msg = "成人"
    
print(msg)