from customer_m1 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)
        
    def get_birthdate(self):
        return self.__birthdate
    birthdate = property(get_birthdate)

if __name__ == '__main__':
    taro = GoldCustomer(101, "斉藤太郎", 180, date(1978, 9, 1))
    
    print(f"{taro.number} {taro.name} 身長: {taro.height}cm "
          f"標準体重: {taro.std_weight():.2f}kg 生年月日: {taro.birthdate}")