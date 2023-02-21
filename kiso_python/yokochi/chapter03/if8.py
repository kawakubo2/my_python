import sys

gender = input('m:男性 f:女性 > ')
if gender not in ('m', 'f'):
    print('性別はmまたはfを選択してください')
    sys.exit()

age = int(input('0以上を入力してください > '))

if gender == 'm' and age <= 20:
    print('2400円です')
elif gender == 'm' and age <= 50:
    print('2800円です')
elif gender == 'm' and age <= 70:
    print('3200円です')
elif gender == 'm' and age > 70:
    print('3600円です')
elif gender == 'f' and age <= 20:
    print('2000円です')
elif gender == 'f' and age <= 50:
    print('2200円です')
elif gender == 'f' and age <= 70:
    print('2400円です')
elif gender == 'f' and age > 70:
    print('2600円です')

if gender == 'm': # 男性の場合
    if age <= 20:
        print('2400円です')
    elif age <= 50:
        print('2800円です')
    elif age <= 70:
        print('3200円です')
    else:
        print('3600円です')
else: # 女性の場合
    if age <= 20:
        print('2000円です')
    elif age <= 50:
        print('2200円です')
    elif age <= 70:
        print('2400円です')
    else:
        print('2600円です')