from customer_m1 import Customer
from datetime import date
class GoldCustomer(Customer):
    def __init__(self, number, name, height = 1, birthdate = 0):
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

if __name__ == '__main__':
    taro = GoldCustomer(101, '斉藤太郎', 180, date(1978, 9, 1))
    # スーパークラスのプロパティ
    name = taro.name
    number = taro.number
    height = taro.height
    # スーパークラスのメソッド
    std_weight = taro.std_weight()
    # サブクラスのプロパティ
    birth = taro.birthdate
    # サブクラスのメソッド
    age = taro.get_age()

    print(f"{number} {name} 身長: {height}cm 標準体重: {std_weight:.2f}kg 誕生日: {birth}")
    print(f"年齢: {age}")



