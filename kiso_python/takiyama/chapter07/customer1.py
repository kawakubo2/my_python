class Customer:
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height
        
taro = Customer(101, "斉藤太郎", 180)
print(f"{taro.number}: {taro.name} {taro.height}cm")

hanako = Customer(102, "山田花子", 160)
print(f"{hanako.number}: {hanako.name} {hanako.height}cm")