from customer_m1 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)

    def get_birthdate(self):
        return self.__birthdate

    def get_age(self):
        now = date.today()
        age = now.year - self.birthdate.year
        if (self.birthdate.month, self.birthdate.day) > (now.month, now.day):
            age -= 1
        return age

    birthdate = property(get_birthdate)
    age = property(get_age)

if __name__ == '__main__':
    taro = GoldCustomer(101, '斎藤太郎', 180, date(2000, 11, 14))
    print('{}さんは{}歳です。'.format(taro.name, taro.age))