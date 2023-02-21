class Customer:
    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height

taro = Customer(101, "斎藤太郎", 180)
print(f"{taro.number}: {taro.name} {taro.height}cm")

taro.height = 175
print(f"{taro.number}: {taro.name} {taro.height}cm")

print(type(taro))