class Calculator:
    def __init__(self, total):
        self.total = total

    def add(self, x):
        self.total += x

    def sub(self, x):
        self.total -= x
        
    def mul(self, x):
        self.total *= x

    def div(self, x):
        self.total /= x

    def get_total(self):
        return self.total

cal = Calculator(0)
cal.add(200)
print(cal.get_total())
cal.sub(100)
print(cal.get_total())
cal.mul(4)
print(cal.get_total())
cal.div(100)
print(cal.get_total())
