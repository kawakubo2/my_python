# my_stats.py
import math

class MyStats:
    def __init__(self, numbers):
        self.numbers = numbers
        self.avg()
        
    def avg(self):
        self.average = sum(self.numbers) / len(self.numbers)
    
    # 分散    
    def variant(self):
        self.variant = sum([(n - self.average) ** 2 for n in self.numbers]) / len(self.numbers)
        return self.variant
    
    # 標準偏差(Standard Deviation)
    def std_dev(self):
        return math.sqrt(self.variant) if self.variant != None else \
            math.sqrt(self.variant(self.numbers))

if __name__ == '__main__':
    fishes = [23, 18, 20, 28, 22, 25, 19, 26, 23, 24]
    mystats = MyStats(fishes)
    variant = mystats.variant()
    std_dev = mystats.std_dev()
    print(f"平均: {mystats.average} 標準偏差: {std_dev:.1f}")
    print(f"この池の○○魚は95%の確からしさで{mystats.average - 2 * std_dev:.1f}～ {mystats.average + 2 * std_dev:.1f}cmの長さである。")
    