# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:09:52 2017

@author: tomok
"""

end = int(input('最後の数値を入力してください: '))

sum = 0
counter = 0

while counter <= end:
    sum += counter
    counter += 1

print(str(end) + 'までの総和:' + str(sum))
