from datetime import date

class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height

    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2

def func1(self):
    print(f"{self.number}: {self.name}")

Customer.show_info = func1

taro = Customer(101, "斎藤太郎", 180)
taro.show_info()