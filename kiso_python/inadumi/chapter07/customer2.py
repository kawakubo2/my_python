# -*- coding: utf-8 -*-

class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
cus1 = Customer(101, '斎藤太郎', 180)
cus2 = Customer(102, '横山花子', 165)

Customer.bmi = 23
print("{}->bmi: {}".format(cus1.name, cus1.bmi))
print("{}->bmi: {}".format(cus2.name, cus2.bmi))