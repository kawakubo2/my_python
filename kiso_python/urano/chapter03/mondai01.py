import sys

gender = input('M.男性 F.女性: ')
if gender not in ('M', 'F'):
    print('性別はMまたはFを入力してください。')
    sys.exit() # プログラム終了

age = int(input('年齢: '))
if age < 0:
    print('年齢は0以上を入力してください。')
    sys.exit()

if age <= 20 and gender == 'M':
    print('2400円')
elif age <= 50 and gender == 'M':
    print('2800円')
elif age <= 70 and gender == 'M':
    print('3200円')
elif age > 70 and gender == 'M':
    print('3600円')
elif age <= 20 and gender == 'F':
    print('2000円')
elif age <= 50 and gender == 'F':
    print('2200円')
elif age <= 70 and gender == 'F':
    print('2400円')
elif age > 70 and gender == 'F':
    print('2600円')

if gender == 'M': # 男性
    if age <= 20:
        print('2400円')
    elif age <= 50:
        print('2800円')
    elif age <= 70:
        print('3200円')
    else:
        print('3600円')
else:             # 女性    
    if age <= 20:
        print('2000円')
    elif age <= 50:
        print('2200円')
    elif age <= 70:
        print('2400円')
    else:
        print('2600円')