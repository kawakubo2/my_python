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

if __name__ == '__main__':    
    ichiro = Customer(103, '鈴木一郎', 175)
    print(f"{ichiro.name} 標準体重: {ichiro.std_weight():.2f}kg")