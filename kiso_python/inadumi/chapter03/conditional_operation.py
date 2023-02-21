# -*- coding: utf-8 -*-

age = int(input('年齢を入力してください:'))

print(str(age) + '歳は' + ('未成年' if age < 20 else '成人'))

if age < 20:
    print(str(age) + '歳は未成年')
else:
    print(str(age) + '歳は生年')

