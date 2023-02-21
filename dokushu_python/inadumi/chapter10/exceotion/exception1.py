import random, math

class A:
    def methodA(self):
        try:
            print('methodA')
            a = self.methodB()
        except ZeroDivisionError as e:
            raise e
        else:
            return a ** math.pi

    def methodB(self):
        try:
            rand_num = random.randrange(5)
            print(f'乱数: {rand_num}')
            b = self.methodC(rand_num)
            print('methodB')
        except ZeroDivisionError as e:
            raise e
        return b * 10
    
    def methodC(self, num):
        print('methodC')
        try:
            return 10 / num
        except ZeroDivisionError as e:
            raise e

try:
    obj = A()
    print(obj.methodA())
except ZeroDivisionError as e:
    print(e)

