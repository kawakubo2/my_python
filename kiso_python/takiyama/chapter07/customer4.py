from datetime import date

class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2;
    
taro = Customer(101, "斉藤太郎", 180)
hanako = Customer(101, "山田花子", 160)
taro.birthdate = date(1989, 7, 3)
print(f"{taro.name} 生年月日: {taro.birthdate}")
# print(f"{hanako.name} 生年月日: {hanako.birthdate}")