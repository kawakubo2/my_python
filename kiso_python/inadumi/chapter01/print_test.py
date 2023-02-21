# -*- coding: utf-8 -*-
#
#
#
#
#

name = '山田五郎'
age = 25

print(name,end='')
print(age)

code=\
"""
if age >= 20:
    print("成人")
else:
    print("未成年")
"""

print(code)

message = \
"""
{}様
    {}年{}月号が発売されました。
    ・・・
"""
name="横山花子"
year=2019
month=7
print(message.format(name, year, month))