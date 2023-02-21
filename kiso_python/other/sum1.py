# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:20:41 2017

@author: tomok
"""

end = int(input("最後の整数を入力してください: "))

sum = 0
for num in range(1, end + 1):
    sum = sum + num
print(str(end) + "までの総和：" + str(sum))
