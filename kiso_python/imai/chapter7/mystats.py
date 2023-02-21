class MyStats:
    def __init__(self, nums):
        self.nums = nums
        self.average = self.avg()

    def avg(self):
        return sum(self.nums) / len(self.nums)

    def variance(self):
        var = self.var = sum([(n - self.average) ** 2 for n in self.nums]) / len(self.nums)
        return var

    def std_dev(self):
        if self.var is None:
            self.var = self.variance()
        return self.var ** 0.5
            
if __name__ == '__main__':
    numbers = [34, 26, 24, 30, 31, 33, 33, 27, 35, 35]
    mystats = MyStats(numbers)
    print('平均: {:.2f} 分散: {:.2f} 標準偏差: {:.2f}'.format(
            mystats.avg(), mystats.variance(), mystats.std_dev()))