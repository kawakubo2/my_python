import dokushu_python.inadumi.chapter08.calc1 as calc

while True:
    sw = int(input("1.加算 2.減算 3.乗算 4.除算 0.終了:  "))
    if sw == 0: break
    if sw == 1:
        calc.add(float(input("数値: ")))
    elif sw == 2:
        calc.sub(float(input("数値: ")))
    elif sw == 3:
        calc.mul(float(input("数値: ")))
    elif sw == 4:
        calc.div(float(input("数値: ")))
    else:
        print("1～4を入力してください")

total = 0
total = calc.get_total()
print(f"合計: {total}")