class Customer:
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

taro = Customer(101, '斉藤太郎', 180)
print(f"{taro.number}: {taro.name} {taro.height}cm")

taro.height = 175
print(f"{taro.number}: {taro.name} {taro.height}cm")