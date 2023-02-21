import random
from abc import abstractmethod, ABC
class AbstractB(ABC):
    @abstractmethod
    def x(self):
        pass
    @abstractmethod
    def y(self):
        pass
    @abstractmethod
    def z(self):
        pass

class B(AbstractB):
    def x(self):
        print('B#x')

    def y(self):
        return random.randrange(100) > 20

    def z(self):
        print('B#z')

class BMock(AbstractB):
    def x(self):
        print('B#x')

    def y(self):
        return random.randrange(100) > 20

    def z(self):
        print('B#z')

class BUltra(AbstractB):
    def x(self):
        print('B#x')

    def y(self):
        return random.randrange(100) > 20

    def z(self):
        print('B#z(爆速バージョン)')
        
class A:
    def __init__(self, b):
        self.b = b

    def run(self):
        self.b.x()
        while self.b.y():
            self.b.z()
            
if __name__ == '__main__':
    a = A(BUltra())
    a.run()





