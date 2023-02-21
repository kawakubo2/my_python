class Member:
    def __init__(self, name, steps_counter):
        self.name = name
        self.steps_counter = steps_counter
        
    def steps_total(self):
        total = 0
        for s in self.steps_counter.values():
            total += s
        return total
    
    def steps_average(self):
        return self.steps_total() / len(self.steps_counter)
    
    def get_steps(self, day):
        try:
            return self.steps_counter.get(day)
        except IndexError:
            print('指定した日付のデータはありません')
    
sc = {1: 5200, 2: 4000, 3:5900, 4:7600, 5:3900}

mem1 = Member('山田太郎', sc)
print('{}さんの今月の総歩数は{}歩で、平均は{:.1f}歩です。'.\
      format(mem1.name, mem1.steps_total(), mem1.steps_average()))

d1 = 6
print('{}日は{}歩です'.format(d1, mem1.get_steps(d1)))

