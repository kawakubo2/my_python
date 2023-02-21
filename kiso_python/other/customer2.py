# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:59:42 2017

@author: tomok
"""

class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
if __name__ == "__main__":
    
    print("bmi: {}".format(Customer.bmi))
    
    taro = Customer(101, "斎藤太郎", 189)
    hanako = Customer(102, "山田花子", 165)
    
    Customer.bmi = 23
    
    print("taro   -> bmi: {}".format(taro.bmi))
    print("hanako -> bmi: {}".format(taro.bmi))