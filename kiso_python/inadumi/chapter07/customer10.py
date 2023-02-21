# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from customer_m2 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)
        
    def get_birthdate(self):
        return self.__birthdate
    
    birthdate = property(get_birthdate)
    
    def get_age(self):
        now = date.today()
        age = now.year - self.birthdate.year
        return age if (self.birthdate.month, self.birthdate.day) <= (now.month, now.day) else age - 1
    
if __name__ == '__main__':
    cus1 = GoldCustomer(101, '斎藤太郎', 180, date(1978, 1, 12))
    print('{} {} 身長:{}cm 標準体重:{:.2f}kg 誕生日:{}'.format(cus1.number, cus1.name,\
          cus1.height, cus1.std_weight(), cus1.birthdate))
    print('年齢: {}'.format(cus1.get_age()))