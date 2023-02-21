# -*- coding: utf-8 -*-

import math
class MyStats:
    def __init__(self, nums):
        self.__nums = nums
        self.get_average
        
    def get_nums(self):
        return self.__nums
    
    def get_average(self):
        avg = sum(self.nums) / len(self.nums)
        self.avg = avg
        return avg
    
    def get_dev(self):
        self.dev = sum([(n - self.avg) ** 2 for n in self.nums]) / len(self.nums)
        return self.dev
            
    def get_std_deviation(self):
        if self.dev is None:
            self.get_dev()
        return math.sqrt(self.dev)
    
    nums = property(get_nums)
    
    
    
if __name__ == '__main__':
    mystats = MyStats([5, 2, 1, 3, 9, 7, 6])
    print('平均:{}'.format(mystats.get_average()))
    print('分散:{}'.format(mystats.get_dev()))
    print('標準偏差:{}'.format(mystats.get_std_deviation()))