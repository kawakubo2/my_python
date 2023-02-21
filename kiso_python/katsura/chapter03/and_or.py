# and_or.py

num = int(input('整数: '))

if (num % 3 == 0 or num % 5 == 0) and num >= 100:
    print('100以上の3または5の倍数')