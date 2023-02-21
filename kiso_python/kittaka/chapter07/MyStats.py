import math
class MyStats:
    def __init__(self, samples):
        self.samples = samples
        self.avg = sum(self.samples) / len(self.samples)
        self.var = None

    def variance(self):
        self.var = sum([(s - self.avg) ** 2 for s in self.samples]) / len(self.samples)
        return self.var

    def std_dev(self):
        if self.var is None:
            return math.sqrt(self.variance())
        else:
            return math.sqrt(self.var) 

if __name__ == '__main__':
    sugaku = [70, 60, 58, 92, 80, 68, 78, 85, 90, 98]
    kokugo = [50, 92, 78, 80, 63, 82, 98, 48, 62, 78]
    rika   = [78, 68, 52, 96, 88, 70, 82, 82, 94, 100]
    
    stat_sugaku = MyStats(sugaku)
    stat_kokugo = MyStats(kokugo)
    stat_rika = MyStats(rika)
    print(f"数学 平均: {stat_sugaku.avg} 分散: {stat_sugaku.variance():.1f} 標準偏差: {stat_sugaku.std_dev():.1f}")
    print(f"国語 平均: {stat_kokugo.avg} 分散: {stat_kokugo.variance():.1f} 標準偏差: {stat_kokugo.std_dev():.1f}")
    print(f"理科 平均: {stat_rika.avg} 分散: {stat_rika.variance():.1f} 標準偏差: {stat_rika.std_dev():.1f}")