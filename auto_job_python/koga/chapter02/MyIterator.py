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

if __name__ == '__main__':
    num_iter = MyIterator([1, 2, 4, 8, 16, 32, 64])

    for num in num_iter:
        print(num)


