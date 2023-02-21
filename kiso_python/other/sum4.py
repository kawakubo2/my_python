 # -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:04:51 2017

@author: tomok
"""

end = int(input('最後の整数を入力してください: '))

sum = 0
for num in range(1, end + 1):
    sum += num

print(str(end) + "の総和:" + str(sum))
