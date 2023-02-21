# -*- coding: utf-8 -*-

from customer_m2 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height = 0, birthdate = 0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)
        
    def get_birthdate(self):
        return self.__birthdate
    
    birthdate = property(get_birthdate)
    
    def get_age(self):
        now = date.today()
        
        age = now.year - self.birthdate.year
        
        if (now.month, now.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
            
        return age
        
    
if __name__ == '__main__':
    taro = GoldCustomer(101, "斉藤太郎", 180, date(1978, 10, 1))
    name = taro.name
    number = taro.number
    height = taro.height
    
    number = taro.number = 99
    
    std_weight = taro.std_weight()
    
    birth = taro.birthdate
    print("{} {} 身長:{}cm 標準体重:{:.2f}kg 生年月日:{}"
          .format(number, name, height, std_weight, birth))
    
    age = taro.get_age()
    print("{} {} 身長:{}cm 標準体重:{:.2f}kg 生年月日:{}"
          .format(number, name, height, std_weight, birth))
    print("年齢:{}".format(age))
    