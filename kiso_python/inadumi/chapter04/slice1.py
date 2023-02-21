# -*- coding: utf-8 -*-

email = input('Eメールアドレスを入力してください : ')
atmark = email.find('@')
if atmark != -1:
    print('ローカル部:{}'.format(email[:atmark]))
    print('ドメイン部:{}'.format(email[atmark + 1:]))
else:
    print(email + 'はEメールアドレスではありません')