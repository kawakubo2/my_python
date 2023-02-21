class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
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

    def set_height(self, height):
        if height <= 0:
            raise Exception("身長が負")

    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2

    name = property(get_name)
    number = property(get_number, set_number)
    height = property(get_height)

try:
    taro = Customer(50, '斎藤太郎', 180)

    taro.number = 200

    print('{}: {} {}cm 標準体重:{:.2f}kg'.format(taro.number, taro.name, taro.height, taro.std_weight()))
except Exception as e:
    print(e)
