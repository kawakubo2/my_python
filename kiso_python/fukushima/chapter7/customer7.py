# -*- coding: utf-8 -*-
class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.__number = number
        self.__name = name
        self.__height = height
        
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        if number < 100:
            raise ValueError('顧客番号は100以下の値は不可')
        self.__number = number
        
    def get_height(self):
        return self.__height
    
    def std_weight(self):
        return Customer.bmi * (self.__height / 100) ** 2
    
    name = property(get_name)
    number = property(get_number, set_number)
    height = property(get_height)

try:
    taro = Customer(101, "斎藤太郎", 180)
    taro.number = 99 # taro.set_number(99)
    print("{}: {} {}cm".format(taro.number, taro.name, taro.height))
except ValueError as e:
    print(e)
