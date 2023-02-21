# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:23:31 2017

@author: tomok
"""

import sys

try:
    age = int(input('年齢を入力してください: '))
    if age >= 13:
        print('大人料金です')
    elif 0 < age < 13:
        print('子供料金です')
    else:
        print('年齢は正の整数です')
except ValueError:
    print('正しい年齢を入力してください')
    sys.exit(-1)

# try:
# 会員テーブルから名前とメールアドレスを取得
# 請求書作成
# 請求書をメールに添付して送信
# except:
# 