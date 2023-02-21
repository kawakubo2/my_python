# -*- coding: utf-8 -*-

class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
    
cus1 = Customer(101, '斎藤太郎', 180)
cus2 = Customer(102, '横山花子', 160)

print('{}: 標準体重: {:.2f}kg'.format(cus1.name, cus1.std_weight()))
print('{}: 標準体重: {:.2f}kg'.format(cus2.name, cus2.std_weight()))