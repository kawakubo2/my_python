# -*- coding: utf-8 -*-

MALE   = 1
FEMALE = 2
OTHER  = 3

prompt = '{}.男性 {}.女性 {}.その他 : '.format(MALE, FEMALE, OTHER)
gender = int(input(prompt))
age = int(input('年齢 : '))

if gender == MALE:
    if age <= 20:
        print('2400円')
    elif age <= 50:
        print('2800円')
    elif age <= 70:
        print('3200円')
    else:
        print('3600円')
elif gender == FEMALE:
    if age <= 20:
        print('2200円')
    elif age <= 50:
        print('2400円')
    elif age <= 70:
        print('2600円')
    else:
        print('2800円')
        
