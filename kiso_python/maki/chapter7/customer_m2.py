# -*- coding: utf-8 -*-

class Customer:
    bmi = 22
    def __init__(self, number, name, height=0):
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
    
    name = property(get_name)
    
    number = property(get_number, set_number)
    
    height = property(get_height)
    
    std_weight = property(std_weight)
    

if __name__ == "__main__":
    print("__name__:", __name__)
    taro = Customer(101, "斎藤太郎", 180)
    print("{} 標準体重: {:.2f}kg".format(taro.name, taro.std_weight()))