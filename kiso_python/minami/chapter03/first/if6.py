age = int(input('年齢を入力してください: '))

if age == 3 or age == 5 or age == 7:
    print('七五三です')

if age in (3, 5, 7):
    print('七五三です')