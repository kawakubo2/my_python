# -*- coding: utf-8 -*-

class Customer:
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
cus1 = Customer(101, "斎藤太郎", 180)
print("{}: {} {}cm".format(cus1.number, cus1.name, cus1.height))

cus1.height = 175
print("{}: {} {}cm".format(cus1.number, cus1.name, cus1.height))