# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:26:35 2017

@author: tomok
"""

email = "tomo.kawakubo@gmail.com"
pos = email.find("@")
print(pos)
local = email[0:pos]
print('ローカル部:' + local)
domain = email[pos + 1:]
print('ドメイン部:' + domain)

langs = ['Python', 'JavaScript', 'Ruby', 'PHP']
str1 = "\t".join(langs)
print(str1)

str2 = "Python,JavaScript,Rubu,PHP"
langs2 = str2.split(",")
for lang in langs2:
    print(lang)
    
str3 = "1,2,3,4,5"
numbers = str3.split(",")
sum = 0
for num in numbers:
    sum += int(num)
print("合計：" + str(sum))
