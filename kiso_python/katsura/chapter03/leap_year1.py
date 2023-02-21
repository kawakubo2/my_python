year = int(input('年: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('閏年です。')
else:
    print('閏年ではありません。')