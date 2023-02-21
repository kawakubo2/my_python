class Customer:
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height

# Customerクラスからtaroインスタンスを生成
taro = Customer(101, '斉藤太郎', 180)
print(f"{taro.number}: {taro.name} {taro.height}cm")

taro.height = 175
print(f"{taro.number}: {taro.name} {taro.height}cm")

ichiro = Customer(201, '鈴木一郎', 182)
print(f"{ichiro.number}: {ichiro.name} {ichiro.height}cm")

