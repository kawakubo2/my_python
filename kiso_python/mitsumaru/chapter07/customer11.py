from datetime import date
from customer_m2 import Customer

class GoldCustomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)

    def get_birthdate(self):
        return self.__birthdate

    def get_age(self):
        now = date.today()
        age = now.year - self.__birthdate.year
        if (self.__birthdate.month, self.__birthdate.day) > (now.month, now.day):
            age -= 1
        return age

    birthdate = property(get_birthdate)
    age = property(get_age)

if __name__ == "__main__":
    taro = GoldCustomer(101, "斎藤太郎", 180, date(2000, 5, 15))
    print(f"{taro.name}さんの年齢は{taro.age}歳です。")