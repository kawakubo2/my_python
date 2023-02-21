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
        if number < 100:
            raise Exception("番号が100より小さい")
        self.__number = number

    def get_height(self):
        return self.__height

    def std_weight(self):
        return Customer.bmi * (self.__height / 100) ** 2

try:
    taro = Customer(101, '斎藤太郎', 180)

    taro.set_number(99)

    print('{}: {} {}cm 標準体重:{:.2f}kg'.format(taro.get_number(), taro.get_name(), taro.get_height(), taro.std_weight()))
except Exception as e:
    print(e)
