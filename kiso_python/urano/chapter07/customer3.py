class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height

    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2

# インスタンスを生成
taro = Customer(101, '斉藤太郎', 180)
hanako = Customer(102, '山田花子', 160)

# 標準体重を表示
print(f"{taro.name} 標準体重: {taro.std_weight():.2f}kg")
print(f"{hanako.name} 標準体重: {hanako.std_weight():.2f}kg")