# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 22:00:48 2017

@author: tomok
"""

half1 = ['春', '夏']
half2 = ['秋', '冬']

season = half1 + half2

print(half1)
print(half2)
print(season)

suit = ['♠', '♣', '♡', '♢']
numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

index = 0
index2 = 0
for num in numbers * 4:
    print("{}{}".format(suit[index2], num))
    index += 1
    if index % 13 == 0:
        index2 += 1
