# -*- coding: utf-8 -*-

year = int(input('生まれた年を入力してください : '))
month = int(input('生まれた月を入力してください : '))
date = int(input('生まれた日を入力してください : '))

# =============================================================================
# if year >= 2020 or year >= 2019 and month >= 6:
#     print('令和生まれですね')
# elif year >= 1989:
#     print('平成生まれですね')
# else:
#     print('昭和以前生まれですね')
#     
# if year <= 1988:
#     print('昭和以前生まれですね')
# elif year <= 2019 and month < 6:
#         print('平成生まれですね')
# else:
#     print('令和生まれですね')
#     
# if (year, month) >= (2019, 6):
#     print('令和生まれですね')
# elif (year, month) >= (1989, 1):
#     print('平成生まれですね')
# else:
#     print('昭和以前生まれですね')
# =============================================================================
now_year = 2020
now_month = 7
now_date = 18

age = now_year - year

if (month, date) > (now_month, now_date):
    age -= 1
    
print('年齢:', age)


