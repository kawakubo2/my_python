month = int(input('月: '))

if month in (12, 1, 2):
    print('冬')
elif month in (3, 4, 5):
    print('春')
elif month in (6, 7, 8):
    print('夏')
elif month in (9, 10, 11):
    print('秋')
else:
    print('1～12の値を入力してください')