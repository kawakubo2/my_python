# -*- coding: utf-8 -*-

class NumList(list):
    def sum_plus_value(self):
        total = 0
        for n in self:
            if n > 0:
                total += n
        return total
    
    def remove_minus_value(self):
        for i in range(len(self)):
            if self[i] < 0:
                self[i] = 0
                
if __name__ == '__main__':
    lst = NumList([1, 2, 3, -4, 9, -9])
    lst[1] = 4
    print("合計: {}".format(lst.sum_plus_value()))
    lst.remove_minus_value()
    print(lst)