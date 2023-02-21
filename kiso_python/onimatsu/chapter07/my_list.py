# -*- coding: utf-8 -*-

class NumList(list):
    def __init__(self, nums):
        super().__init__(nums)
        
    def sum_plus_value(self):
        sum = 0
        for n in self:
            if n > 0:
                sum += n
        return sum
    
    def remove_minus_value(self):
        for i in range(len(self)):
            if self[i] < 0:
                self[i] = 0
            
if __name__ == '__main__':
    num_list = NumList([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    num_list[1] = -5
    
    print('プラスの合計:{}'.format(num_list.sum_plus_value()))
    
    num_list.remove_minus_value()
    print(num_list)
    
    num_list2 = [n * n for n in num_list]
    print(num_list2)
    
    print('リストの件数:{}'.format(len(num_list)))
    num_list.append(10)
    print('リストの件数:{}'.format(len(num_list)))
    
    