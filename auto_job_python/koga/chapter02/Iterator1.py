class MyIterator:
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == len(self._numbers):
            raise StopIteration()
        result = self._numbers[self._index]
        self._index += 1
        return result
        
class EvenIterator:
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._index == len(self._numbers):
                raise StopIteration()
            result = self._numbers[self._index]
            self._index += 1
            if result % 2 == 0:
                return result

class PositiveIterator:
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._index == len(self._numbers):
                raise StopIteration()
            result = self._numbers[self._index]
            self._index += 1
            if result > 0:
                return result
        
if __name__ == '__main__':
    my_iter = PositiveIterator([1, 2, -3, 4, 5, -6, 7, 8, 9, -10, 11, 12])
    """
    try:
        while True:
            print(next(my_iter))
    except:
        pass
    """
    for n in my_iter:
        print(n)
