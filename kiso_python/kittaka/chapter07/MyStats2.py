import math
from MyStats import MyStats
class MyStats2:
    def __init__(self, samples1, samples2):
        self.samples1 = samples1
        self.samples2 = samples2
        self.avg1 = sum(self.samples1) / len(self.samples1)
        self.avg2 = sum(self.samples2) / len(self.samples2)

    def coef(self):
        samples1_stat = MyStats(self.samples1)
        samples2_stat = MyStats(self.samples2)
        return sum([(v1 - self.avg1)*(v2 - self.avg2) for v1, v2 in zip(self.samples1, self.samples2)]) / len(self.samples1) \
            / (samples1_stat.std_dev() * samples2_stat.std_dev())

if __name__ == '__main__':
    sugaku = [70, 60, 58, 92, 80, 68, 78, 85, 90, 98]
    kokugo = [50, 92, 78, 80, 63, 82, 98, 48, 62, 78]
    rika   = [78, 68, 52, 96, 88, 70, 82, 82, 94, 100]
    
    sugaku_kokugo = MyStats2(sugaku, kokugo)
    sugaku_rika   = MyStats2(sugaku, rika)
    kokugo_rika = MyStats2(kokugo, rika)
    print(f"数学と国語の相関係数: {sugaku_kokugo.coef():.1f}")
    print(f"数学と理科の相関係数: {sugaku_rika.coef():.1f}")
    print(f"国語と理科の相関係数: {kokugo_rika.coef():.1f}")