# -*- coding: utf-8 -*-

words1 = {'空', '海', '川', '地球'}
words2 = {'山', '海', '空', '空気'}

#　和
print(words1 | words2)

# 積
print(words1 & words2)

# 差
print(words1 - words2)

# 排他的論理和
print(words1 ^  words2)

ingradients = {'ジャガイモ', 'ニンジン', 'ブタニク', 'ショウユ', 'ミリン'}
reizouko = {'ジャガイモ', 'ギュウニュウ', 'トマト', 'サバ', 'ニンジン', 'ブタニク', 'ショウユ', 'ミリン'}

if ingradients.issubset(reizouko):
    print('作れる')
else:
    print('残念、足りない材料があります')