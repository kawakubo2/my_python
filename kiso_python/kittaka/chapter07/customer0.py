import sys

class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.__name = name
        self.__height = height
        
    @property
    def get_name(self):
        return self.__name
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        if value <= 100:
            raise ValueError("引数が100未満")
        self.__number = number
        
    @property
    def height(self):
        return self.__height
    
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
    
taro = Customer(100, "斉藤太郎", 180)

name = taro.name # 内部ではget_name()が動いている
try:
    taro.number = 99 # 内部ではset_number(99)が動いている
except ValueError as e:
    print(e)
number = taro.number # 内部ではget_number()が動いている
height = taro.height # 内部ではget_height()が動いている

print(f"{number}: {name} {height}cm")

 
        
        