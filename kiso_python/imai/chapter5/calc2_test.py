# -*- coding: utf-8 -*-

from calc2 import MyCalc

calc = MyCalc()

while True:
    sw = int(input("1.加算 2.減算 3.乗算 4.除算 9.終了 : "))
    if sw == 9:
        break
    num = int(input('数値: '))
    if sw == 1:
        calc.add(num)
    elif sw == 2:
        calc.sub(num)
    elif sw == 3:
        calc.mul(num)
    elif sw == 4:
        calc.div(num)
    else:
        print("1～4を入力してください")
    print(calc.getTotal())