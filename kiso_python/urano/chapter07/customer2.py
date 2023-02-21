class Customer:
    bmi = 22 # クラス変数
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height

print(f"bmi: {Customer.bmi}")

# インスタンスを生成
taro = Customer(101, '斉藤太郎', 180)
hanako = Customer(102, '山田花子', 175)

# クラス変数の値を変更
Customer.bmi = 23
print(f"taro -> bmi: {taro.bmi}")
print(f"hanako -> bmi: {hanako.bmi}")