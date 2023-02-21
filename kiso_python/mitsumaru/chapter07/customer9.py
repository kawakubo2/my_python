from kiso_python.mitsumaru.chapter07.customer_m2 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number, name, height)

    def get_birthdate(self):
        return self.__birthdate

    birthdate = property(get_birthdate)

if __name__ == "__main__":

    taro = GoldCustomer(101, "斎藤太郎", 180, date(1978, 9, 1))

    name = taro.name
    number = taro.number
    height = taro.height
    std_weight = taro.std_weight()
    birth = taro.get_birthdate()

    print(f"{number} {name} 身長:{height}cm 標準体重:{std_weight}kg 生年月日:{birth}")