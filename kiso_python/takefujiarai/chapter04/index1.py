# -*- coding: utf-8 -*-

words = ['空', '秘密', '電柱', 'ひらけごま', '海', 'ギター']

str = input('文字列を入力してください: ')

try:
    index = words.index(str)
    print('"{}"のインデックスは{}です'.format(str, index))
except ValueError:
    print('"{}"は見つかりませんでした'.format(str))
    
names = ['山田', '井上', '太田', '田中']

names[1] = '江藤'
# names[9] = '加藤'
print(names)

lst = []
lst.append('春')
lst += ['夏', '秋', '冬']
print(lst)

score = [
 [70, 65, 82, 90, 58],
 [88, 50, 79, 82, 69],
 [93, 73, 52, 79, 90]
]
# 一番下の行の右から2番目の７９を取り出すには
print(score[2][3])