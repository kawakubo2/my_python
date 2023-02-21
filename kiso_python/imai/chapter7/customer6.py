class Customer:
    bmi = 22
    def __init__(self, number, name, height = 0):
        self.number = number
        self.name = name
        self.height = height

    def std_weight(self):
        return Customer.bmi * (self.height / 100) ** 2


taro = Customer(101, '斎藤太郎', 180)
hanako = Customer(102, '山田花子', 165)

Customer.LIMIT = 50

print(taro.LIMIT)
print(hanako.LIMIT)
print(Customer.LIMIT)

Customer.show_info = lambda self: print('{}: {}'.format(self.number, self.name))

taro.show_info()
hanako.show_info()

Customer.abc = lambda self: print(self.name[:3])

taro.abc()