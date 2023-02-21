class NumList(list):
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
    lst = NumList([1, 2, 3, -1, 9, -9])
    lst[1] = 4
    print(f"合計: {lst.sum_plus_value()}")
    lst.remove_minus_value()
    print(lst)