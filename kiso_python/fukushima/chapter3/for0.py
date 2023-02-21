# -*- coding: utf-8 -*-

nums = [1, 2, 3, 4, 5, 6]

itr = iter(nums)

while True:
    try:
        print(next(itr))
    except:
        break
    
# 糖衣構文(シンタックス・シュガー)
for n in nums:
    print(n)