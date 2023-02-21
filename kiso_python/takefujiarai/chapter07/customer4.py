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
    
taro = Customer(101, "斉藤太郎", 180)

taro.birthdate = date(1989, 7, 3)
print('{}: 生年月日:{}'.format(taro.name, taro.birthdate))