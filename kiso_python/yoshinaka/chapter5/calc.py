total = 0

def add(x):
    global total
    total += x
def sub(x):
    global total
    total -= x
def mul(x):
    global total
    total *= x
def div(x):
    global total
    total /= x

while True:
    sw = int(input('1.加算 2.減算 3.乗算 4.除算 9.終了'))
    if sw == 9:
        break
    if sw == 1:
        x = float(input('数値'))
        add(x)
        print(total)
    elif sw == 2:
        x = float(input('数値'))
        sub(x)
        print(total)
    elif sw == 3:
        x = float(input('数値'))
        mul(x)
        print(total)
    elif sw == 4:
        x = float(input('数値'))
        div(x)
        print(total)

