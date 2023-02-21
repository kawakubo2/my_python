# monday1.py
import sys
gender = int(input('1.男性 2.女性'))
if gender not in(1, 2):
    print('性別は1または2を入力してください')
    sys.exit()

age = int(input('年齢:'))
if age < 0:
    print('年齢は0以上を入力して下さい。')

if gender == 1 and age <= 20:
    print('2400円')
elif gender == 1 and age <= 50:
    print('2800円')
elif gender == 1 and age <= 70:
    print('3200円')
elif gender == 1 and age > 70:
    print('3600円')
elif gender == 2 and age <= 20:
    print('2000円')
elif gender == 2 and age <= 50:
    print('2200円')
elif gender == 2 and age <= 70:
    print('2400円')
elif gender == 2 and age > 70:
    print('2600円')

if gender == 1:
    if age <= 20:
        print('2400円')
    elif age <= 50:
        print('2800円')
    elif age <= 70:
        print('3200円')
    else:
        print('3600円')
else:
    if age <= 20:
        print('2000円')
    elif age <= 50:
        print('2200円')
    elif age <= 70:
        print('2400円')
    else:
        print('2600円')

