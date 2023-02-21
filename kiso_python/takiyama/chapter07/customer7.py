class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.__number = number
        self.__name = name
        self.__height = height
        
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        self.__number = number
        
    def get_height(self):
        return self.__height
    
    def std_weight(self):
        return Customer.bmi * (self.__height / 100) ** 2
    
taro = Customer(101, "斉藤太郎", 180)

# name = taro.__name

taro._Customer__name = "斉藤次郎"

name = taro.get_name()
taro.set_number(99)
number = taro.get_number()
height = taro.get_height()
print(f"標準体重: {taro.std_weight()}")


print(f"{number}: {name} {height}cm")