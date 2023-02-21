year = int(input('年: '))

if (year % 4 == 0 and year % 4 != 100) or year % 400 == 0:
    print(str(year) + 'は閏年です。')
else:
    print(str(year) + 'は閏年ではありません。')