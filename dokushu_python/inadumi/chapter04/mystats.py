class MyStats:
    def __init__(self, nums):
        self.nums = nums
        self.avg = self.average()

    def average(self):
        return sum(self.nums) / len(self.nums)        

    def variance(self):
        self.var = sum([(n - self.avg) ** 2 for n in self.nums]) / len(self.nums)
        return self.var

    def std_dev(self):
        if not self.var:
            self.var = self.variance()
        return self.var ** 0.5

if __name__ == '__main__':
    numbers = [31, 28, 29, 30, 33, 27, 30, 29, 29, 31]
    stats = MyStats(numbers)
    print('平均: {:.2f} 分散: {:.2f} 標準偏差: {:.2f}'.format(stats.average(), stats.variance(), stats.std_dev()))