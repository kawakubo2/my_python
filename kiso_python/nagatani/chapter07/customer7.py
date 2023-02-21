from datetime import date

class Customer:
    bmi = 22 # クラス変数
    # __slots__ = ['number', 'name', 'height']
    def __init__(self, number, name, height = 0):
        self.__number = number
        self.__name = name
        self.__height = height

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_number(self, number): 
        if number < 0:
            raise Exception("番号が負")
        self.__number = number

    def get_height(self):
        return self.__height

    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2

    name = property(get_name)
    number = property(get_number, set_number)
    height = property(get_height)

def show_info(self):
    print(f"{self.number}: {self.name}")

taro = Customer(101, '斉藤太郎', 180)

Customer.show_info = show_info

hanako = Customer(102, '山田花子', 160)
hanako.number = 202
taro.show_info()
hanako.show_info()
print(hanako.name)

taro.birthdate = date(2000, 1, 1)
print(taro.birthdate)