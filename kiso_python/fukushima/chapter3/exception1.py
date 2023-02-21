# -*- coding: utf-8 -*-

from input_util import input_range

score = input_range(0, 100, '点数を入力してください')

if score >= 80:
    print('合格')
else:
    print('不合格')