# -*- coding: utf-8 -*-

month = int(input('月の値を入力してください : '))

if month in (12, 1, 2):
    print('冬')
elif month in (3, 4, 5):
    print('春')
elif month in (6, 7, 8):
    print('夏')
elif month in (9, 10, 11):
    print('秋')
else:
    print('1～12の値を入力してください')
    
msg = ''

age = 18

# =============================================================================
# if age < 20:
#     msg = '未成年'
# else:
#     msg = '成人'
# =============================================================================
    
msg = '未成年' if age < 20 else '成人'

print(msg)