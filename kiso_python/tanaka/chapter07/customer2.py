class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
if __name__ == '__main__':
    print(f"bmi: {Customer.bmi}")
    
    taro = Customer(101, "斉藤太郎", 180)
    hanako = Customer(102, "山田花子", 165)

    Customer.bmi = 23
    
    print(f"taro -> bmi: {taro.bmi}")
    print(f"hanako -> bmi: {hanako.bmi}")