# -*- coding: utf-8 -*-

str1 = '水金地火木土'

str2 = input('検索文字列を入力してください : ')

if str2 in str1:
    print("'{}'が見つかりました。".format(str2))
else:
    print("'{}'が見つかりませんでした。".format(str2))
    
    
nums = [123332.34342242, +371242.893283, 4245489.3983819, 4242771.94189]
names = ['Yamada', 'Yokoyama', 'Tanaka', 'Yamamoto']

for num, name in zip(nums, names):
    print("{:10s}:{:12,.2f}".format(name, num))
    
