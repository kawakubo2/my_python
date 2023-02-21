# -*- coding: utf-8 -*-

nums = [1, 2, 3, 4]

for n in nums:
    print(n)

print('--------')
  
for i in range(len(nums)):
    print(nums[i])

# for ... in イテレート可能なオブジェクト

season = ['春', '夏', '秋', '冬']

itr = iter(season)

try:
    while(True):
        print(next(itr))
    
except StopIteration:
    pass

print('-------------')

for s in season:
    print(s)
    
# 糖衣後部