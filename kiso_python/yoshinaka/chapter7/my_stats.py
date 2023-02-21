class MyStats:
    def __init__(self, nums):
        self.__nums = nums
        self.__avg = sum(nums) / len(nums)

    def get_avg(self):
        return self.__avg

    def get_variance(self):
        self.var = sum([(n - self.__avg) ** 2 for n in self.__nums]) / len(self.__nums)
        return self.var

    def get_std_dev(self):
        if self.var is None:
            self.var = self.variance()
        return self.var ** 0.5

    avg = property(get_avg)
    variance = property(get_variance)
    std_dev = property(get_std_dev)

if __name__ == '__main__':
    cms = [30, 29, 28, 33, 29, 30, 31, 27, 28, 29]
    mystats = MyStats(cms)
    print('平均: {:.2f} 分散:{:.2f} 標準偏差:{:.2f}'.format(mystats.avg, mystats.variance, mystats.std_dev))
