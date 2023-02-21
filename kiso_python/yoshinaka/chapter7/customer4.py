from datetime import date

class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name  = name
        self.height = height

    def std_weight(self):
        """
        bmi = weight / height ** 2  ---> weight = bmit * height ** 2
        """
        return Customer.bmi * (self.height / 100) ** 2

# インスタンスを生成
taro = Customer(101, '斎藤太郎', 180)
taro.birthdate = date(1989, 7, 3)
print('{} 誕生日:{}'.format(taro.name, taro.birthdate))