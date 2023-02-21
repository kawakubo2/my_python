class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
    
taro = Customer(101, "斉藤太郎", 180)
hanako = Customer(102, "山田花子", 160)
#def show_info(self):
#    print(f"{self.number}: {self.name}")
    
Customer.show_info = lambda self: print(f"{self.number}: {self.name}")

taro.show_info()
hanako.show_info()