# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:43:18 2017

@author: tomok
"""
from datetime import date

class Customer:
    bmi = 22
    
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name =  name
        self.height = height
        
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2

class Customer2:
    bmi = 22
    
    def __init__(self, number, name, height):
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
        return Customer2.bmi * (self.__height / 100) ** 2

class Customer3:
    bmi = 22
    def __init__(self, number, name, height):
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
        return Customer3.bmi * (self.height / 100) ** 2

    number = property(get_number, set_number)
    name = property(get_name)
    height = property(get_height)

from datetime import date

class GoldCustomer(Customer):
	def __init__(self, number, name, height, birthdate = 0):
		self.__birthdate = birthdate
		super().__init__(number, name, height)
	
	def get_birthdate(self):
		return self.__birthdate
		
	def get_age(self):
		now = date.today()
		age = now.year - self.birthdate.year
		if (now.month, now.day) >= (self.birthdate.month, self.birthdate.day):
			return age
		else:
			return age - 1

	birthdate = property(get_birthdate)

    