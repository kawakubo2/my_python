# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:20:26 2017

@author: tomok
"""

taro = 170.0
ichiro = 165.5
makoto = 181.5
average = (taro + ichiro + makoto) / 3
print("平均身長：{}cm".format(average))

members = {'taro': 170.0, 'ichiro': 165.5, 'makoto': 181.5}
sum = 0
for name, height in members.items():
    print("{:10}{:5.1f}cm".format(name, height))
    sum += height
print("average   {:5.1f}cm".format(sum / len(members)))