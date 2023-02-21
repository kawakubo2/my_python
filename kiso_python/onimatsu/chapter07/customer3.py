# -*- coding: utf-8 -*-
from datetime import date


class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
    
Customer.LIMIT = 50

def show_info(self):
    print('{}: {}'.format(self.number, self.name))

taro = Customer(101, '斉藤太郎', 180)
hanako = Customer(102, '山田花子', 160)

Customer.show_info = show_info

ichiro = Customer(103, '鈴木イチロー', 183)

print('{} 標準体重:{:.2f}kg'.format(taro.name, taro.std_weight()))
print('{} 標準体重:{:.2f}kg'.format(hanako.name, hanako.std_weight()))

taro.birthdate = date(1989, 7, 3)
print('{} 生年月日:{}'.format(taro.name, taro.birthdate))

print(taro.LIMIT)
print(hanako.LIMIT)
print(Customer.LIMIT)

taro.show_info()
hanako.show_info()
ichiro.show_info()
