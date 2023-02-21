import re

bunshi = int(input('分子: '))

while True:
    try:
        bunbo = int(input('分母: '))
        if bunbo == 0:
            print('分母は0以外を入力してください')
            continue
        print(f"{bunshi} / {bunbo} = {bunshi/bunbo}")
        break
    except ValueError:
        print('整数値を入力してください。')
    
    
    
    
    
    
    
