# -*- coding: utf-8 -*-

from customer_m2 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height, birthdate):
        self.__birthdate = birthdate
        super().__init__(number, name, height)
        
    def get_birthdate(self):
        return self.__birthdate
    
    birthdate = property(get_birthdate)
    
    def get_age(self):
        now = date.today()
        
        age = now.year - self.birthdate.year
        
        if (now.month, now.day) >= (self.birthdate.month, self.birthdate.day):
            return age
        else:
            return age - 1
        
    age = property(get_age)
        
if __name__  == "__main__":
    taro = GoldCustomer(101, "斎藤太郎", 180, date(1978, 9, 1))
    
    print("{} {} 身長:{}cm 標準体重:{:.2f}kg 誕生日:{}".format(
            taro.number, taro.name, taro.height, 
            taro.std_weight, taro.birthdate))
    
    print("年齢: {}".format(taro.age))
            