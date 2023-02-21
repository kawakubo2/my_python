# -*- coding: utf-8 -*-

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
        return Customer.bmi * (self.height / 100) ** 2
    
    name = property(get_name)
    number = property(get_number, set_number)
    height = property(get_height)
    
cus1 = Customer(101, '斎藤太郎', 180)
cus1.number = 99
print('{}: {} {}cm'.format(cus1.number, cus1.name, cus1.height))
    
        