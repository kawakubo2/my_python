from customer_m1 import Customer
from datetime import date

class GoldCustomer(Customer):
    def __init__(self, number, name, height=0, birthdate=0):
        self.__birthdate = birthdate
        super().__init__(number,name,height)
        
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

if __name__ == '__main__':
    taro = GoldCustomer(101, '斉藤太郎', 180, date(1978, 9, 1))
    name = taro.name
    number = taro.number
    height = taro.height
    std_weight = taro.std_weight()
    birth = taro.birthdate
    age = taro.age
    
    print(f'{number} {name} 身長:{height}cm 標準体重:{std_weight:.2f}kg 生年月日:{birth}')
    print(f'年齢:{age}歳')
