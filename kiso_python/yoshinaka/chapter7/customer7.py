class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.set_number(number)
        self.__name = name
        self.__height = height
    
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_number(self, number):
        if number <= 0:
            raise Exception('numberが負数')
        self.__number = number

    def get_height(self):
        return self.__height

    def std_weight(self):
        return Customer.bmi * (self.__height / 100) ** 2


# name = taro.__name 
# number = taro.__number 

try:
    taro = Customer(-101, '斎藤太郎', 180)
    name = taro.get_name()
    taro.set_number(-1)
    number = taro.get_number() 
    height = taro.get_height()
    print('{}: {} {}cm'.format(number, name, height))
except Exception as e:
    print(e)