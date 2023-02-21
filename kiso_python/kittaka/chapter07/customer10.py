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
        if (now.month, now.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

if __name__ == '__main__':
    
    taro = GoldCustomer(101, "斉藤太郎", 180, date(1978, 9, 1))
    
    print(f"{taro.number} {taro.name} 身長: {taro.height}cm "
          f"標準体重: {taro.std_weight():.2f}gh 生年月日: {taro.birthdate}")
    print(f"年齢: {taro.get_age()}")