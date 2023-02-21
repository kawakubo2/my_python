# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:58:06 2017

@author: tomok
"""

from customer import Customer
from datetime import date
# インスタンスを生成
taro = Customer(101, "斎藤太郎", 180)
# インスタンス変数を追加
taro.birthdate = date(1989, 7, 2)
print("{} 生年月日:{}".format(taro.name, taro.birthdate))
