# -*- coding: utf-8 -*-

words = ['冬', '秘密', '電柱', 'ひらけごま', '海', 'ギター']

str1 = input('文字列を入力してください : ')

try:
    index = words.index(str1)
    print('"{}"のインデックスは{}です'.format(str1, index))
except ValueError:
    print('"{}"は見つかりませんでした'.format(str1))
    
words[0] = '夏'

print(words)

nums = [1, 2, [3, 4, [5, 6], 7], [8, 9], 10]