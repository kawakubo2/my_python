class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
    
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2

def show_info(self):
    print("{}: {} {}cm".format(self.number, self.name, self.height))

Customer.show = show_info
taro = Customer(101, "斉藤太郎", 180)
taro.show()
taro.height = 182
taro.show()

hanako = Customer(102, "山田花子", 165)
hanako.show()
