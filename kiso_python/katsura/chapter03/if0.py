import sys

sex = input('F.女性 M.男性: ')
if sex not in ('F', 'M'):
    print('性別はFまたはMで入力してください')
    sys.exit()

age = int(input('年齢を入力してください: '))
if age < 0:
    print('年齢は0以上を入力してください。')
    sys.exit()

if sex == 'F':
    if age <= 20:
        price = 2000
    elif age <= 50:
        price = 2200
    elif age <= 70:
        price = 2400
    else:
        price = 2600
else:
    if age <= 20:
        price = 2400
    elif age <= 50:
        price = 2800
    elif age <= 70:
        price = 3200
    else:
        price = 3600




