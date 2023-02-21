import sys, math

gender = int(input('1.女性 2.男性: '))
if gender not in (1, 2):
    print('性別は1または2で入力してください。')
    sys.exit()

age = int(input('年齢: '))
if age < 0:
    print('年齢は0以上を入力してください。')
    sys.exit()

if gender == 1 and age <= 20:
    print('2000円')
elif gender == 1 and age <= 50:
    print('2200円')
elif gender == 1 and age <= 70:
    print('2400円')
elif gender == 1 and age > 70:
    print('2600円')
elif gender == 2 and age <= 20:
    print('2400円')
elif gender == 2 and age <= 50:
    print('2800円')
elif gender == 2 and age <= 70:
    print('3200円')
elif gender == 2 and age > 70:
    print('3600円')
else:
    pass

if gender == 1: # 女性の場合
    if age <= 20:
        price = 2000
    elif age <= 50:
        price = 2200
    elif age <= 70:
        price = 2400
    else:
        price = 2600
else: # 男性の場合
    if age <= 20:
        price = 2400
    elif age <= 50:
        price = 2800
    elif age <= 70:
        price = 3200
    else:
        price = 3600

print('料金は' + str(price) + '円です。')
print('料金は%dです。' % (price))
print('料金は{}円です。'.format(price))
print(f'料金は{price}円です。')

name = '山田太郎'
age = 32
weight = 72
height =  172

print(f'{name}({age}歳)のBMI値は{weight / (height / 100) ** 2:.1f}です。')