gender = input('性別 F:女性 M:男性 X:その他 : ')
age = int(input('年齢: '))

if gender == 'M' and age <= 20:
    print('2400円です')
elif gender == 'M' and age <= 50:
    print('2800円です')
elif gender == 'M' and age <= 70:
    print('3200円です')
elif gender == 'M' and age > 70:
    print('3600円です')
if gender == 'F' and age <= 20:
    print('2000円です')
elif gender == 'F' and age <= 50:
    print('2200円です')
elif gender == 'F' and age <= 70:
    print('2400円です')
elif gender == 'F' and age > 70:
    print('2600円です')


if gender == 'M':
    if age <= 20:
        print('2400円')
    elif age <= 50:
        print('2800円')
    elif age <= 70:
        print('3200円')
    else:
        print('3600円')
elif gender == 'F':
    if age <= 20:
        print('2000円')
    elif age <= 50:
        print('2200円')
    elif age <= 70:
        print('2400円')
    else:
        print('2600円')