class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2
    
def show_info(self):
    print(f"{self.number}: {self.name}")

taro = Customer(101, "斉藤太郎", 180)

Customer.show_info = show_info
    
taro.show_info()

hanako = Customer(102, "山田花子", 160)
hanako.show_info()