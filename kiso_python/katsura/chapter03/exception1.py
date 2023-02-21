# exception1.py

def div(a, b):
    return a / b

while True:
    try:
        a = int(input('a: '))
        b = int(input('b: '))
        print(div(a, b))
        break
    except ZeroDivisionError:
        print("0で割ろうとしました。")
    except ValueError:
        print("数値を入力してください")
