class Customer:
    bmi = 22 # クラス変数
    """
    __init__メソッド(コンストラクタ)の主な役割は
    インスタンス変数に値を代入することである。
    コンストラクタで値を代入することを
    コンストラクタインジェクションと呼ぶ
    """
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height

print(f"bmi: {Customer.bmi}")

taro = Customer(101, '斉藤太郎', 180)
hanako = Customer(102, '山田花子', 165)

Customer.bmi = 23

print(f"{taro.number}: {taro.name} {taro.height}cm")

print(f"taro -> bmi: {taro.bmi}")
print(f"hanako-> bmi: {hanako.bmi}")