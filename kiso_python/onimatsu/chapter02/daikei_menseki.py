# -*- coding: utf-8 -*-

print('台形の計算をします。')

upper_base = float(input('上底を入力してください: '))
lower_base = float(input('下底を入力してください: '))
height     = float(input('高さを入力してください: '))

print('上底が' + str(upper_base) + '、下底が' + str(lower_base) + 
      '、高さが' + str(height) + 'の台形の面積は' + 
      str((upper_base + lower_base) * height / 2))

print('上底が{}、下底が{}、高さが{}の台形の面積は{}'.format(upper_base,
      lower_base, height, (upper_base + lower_base) * height / 2))
