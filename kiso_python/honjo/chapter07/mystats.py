# -*- coding: utf-8 -*-

class MyStats:
    def __init__(self, numbers):
        self.__numbers = numbers
        
        
    def mean(self):
        return sum(self.__numbers) / len(self.__numbers)
    
    def variance(self):
        mean = self.mean()
        return sum([(num - mean) ** 2 for num in self.__numbers]) \
            / len(self.__numbers)
            
    def std(self):
        return self.variance() ** 0.5
    
    def coef(self, others):
        other_stats = MyStats(others)
        o_mean = other_stats.mean()
        o_std = other_stats.std();
        s_mean = self.mean()
        s_std = self.std()
        numerator = sum([(s - s_mean) * \
            (o - o_mean) for s, o in zip(self.__numbers, others)]) / len(self.__numbers)
        denominator = s_std * o_std
        return numerator / denominator
    
if __name__ == '__main__':
    stats = MyStats([66, 57, 62, 55, 64, 62, 50, 66, 61, 57])
    
    print("平均:{:.1f}".format(stats.mean()))
    print("分散:{:.1f}".format(stats.variance()))
    print("標準偏差:{:.1f}".format(stats.std()))
    
    print("相関係数:{:.3f}".format(stats.coef([38, 28, 38, 20, 32, 31, 20, 36, 30, 28])))
    print("相関係数:{:.3f}".format(stats.coef([58, 100, 72, 48, 18, 79, 28, 8, 92, 10])))
    
    stats2 = MyStats([2400, 3100, 1800, 1200, 3500, 1900, 2000, 2000, 1500, 3500])
    print("築年数とマンション価格の相関係数:{:.3f}".format(stats2.coef([12, 8, 23, 35, 7, 25, 29, 19, 30, 11])))
