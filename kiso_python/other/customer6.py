# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:07:39 2017

@author: tomok
"""
from customer import Customer

goro = Customer(102, "田中五郎", 187)

def show_info(self):
    print("{}: {}".format(self.number, self.name))


# 道的にインスタンスメソッドを追加
Customer.show_info = show_info

taro = Customer(100, "山田太郎", 180)
jiro = Customer(101, "鈴木次郎", 178)

taro.show_info()
jiro.show_info()
goro.show_info()
