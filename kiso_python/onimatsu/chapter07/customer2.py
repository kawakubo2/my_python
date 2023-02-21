# -*- coding: utf-8 -*-

class Customer:
    bmi = 22
    def __init__(self,number,name,height=0):
        self.number=number
        self.name=name
        self.height=height

print('bmi: {}'.format(Customer.bmi))  
      
taro = Customer(101, '斉藤太郎', 180)
hanako = Customer(102,'山田花子', 165)

Customer.bmi = 23
print('taro -> bmi: {}'.format(taro.bmi))
print('hanako -> bmi: {}'.format(hanako.bmi))