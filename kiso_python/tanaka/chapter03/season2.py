month = int(input('月: '))

if month == 12 or month == 1 or month == 2:
    print(str(month) + '月は冬です。')
elif 3 <= month <= 5:
    print(str(month) + '月は春です。')
elif 6 <= month <= 8:
    print(str(month) + '月は夏です。')
elif 9 <= month <= 11:
    print(str(month) + '月は秋です。')
else:
    print('1～12の値を入力してください。')