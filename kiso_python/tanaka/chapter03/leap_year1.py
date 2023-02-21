year = int(input('年を整数で入力してください: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(str(year) + 'は閏年です')
else:
    print(str(year) + 'は閏年ではありません。')