class Customer:
    bmi = 22
    def __init__(self, number, name, height=0):
        self.set_number(number)
        self.__name = name
        self.__height = height
        
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        if number < 1:
            raise Exception('会員番号は1以上です。')
        self.__number = number
        
    def get_height(self):
        return self.__height
    
    def std_weight(self):
        return Customer.bmi * (self.__height / 100) ** 2
    
    # プロパティ
    name = property(get_name)
    number = property(get_number, set_number)
    height = property(get_height)
    
taro = Customer(101, '斉藤太郎', 180)

# name = taro.__name
# number = taro.__number

try:
    name = taro.name
    taro.number = 99
    number = taro.number
    height = taro.height

    print(f"{number}: {name} {height}cm 標準体重: {taro.std_weight()}kg")
except Exception as e:
    print(e)