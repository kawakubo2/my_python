# -*- coding: utf-8 -*-

class StepsCalculator:
    def __init__(self, name, steps):
        self.name = name
        self.steps = steps
        
    def step_total(self):
        total = 0
        for step in self.steps.values():
            total += step
            
        return total
    
    def step_average(self):
        return self.step_total() / len(self.steps)
    
    def get_step_by_date(self,d):
        if d > len(self.steps):
            print('{}日でデータは存在しません'.format(d))
            return 0
        return self.steps[d]

sc1 = StepsCalculator('山田太郎',\
    {1:6200, 2:7800, 3:0, 4:5900})

print('{}さんの総歩数は{}歩'.format(sc1.name, sc1.step_total()))
print('平均は{:.1f}歩'.format(sc1.step_average()))

d1 = 1
print('{}日の歩数は{}歩です'.format(d1, sc1.get_step_by_date(d1)))