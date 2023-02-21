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
            if result <= 0:
                continue
            return result

if __name__ == '__main__':
    num_iter = MyIterator([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    # 糖衣構文(シンタックスシュガー)
    for n in num_iter:
        print(n)


    positive_iter = PositiveIterator([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
    print('---< next関数で取り出す >---')
    try:
        while True:
            print(next(positive_iter))
    except StopIteration:
        pass