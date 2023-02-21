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
        self.__number = number
        
    def get_height(self):
        return self.__height
    
    def std_weight(self):
        return Customer.bmi * (self.__height / 100) ** 2
        
cus1 = Customer(101, '斎藤太郎', 180)
cus1.set_number(99)
print('{}: {} {}cm'.format(cus1.get_number(), cus1.get_name(), cus1.get_height()))
    
        