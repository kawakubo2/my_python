month = int(input('月: '))

if month in (12, 1, 2):
    print(str(month) + '月は冬です。')
elif month in (3, 4, 5):
    print(str(month) + '月は春です。')
elif month in (6, 7, 8):
    print(str(month) + '月は夏です。')
elif month in (9, 10, 11):
    print(str(month) + '月は秋です。')
else:
    print('1～12の値を入力してください。')