from mylist import MyList

lst = MyList([1, 2, 3, -4, 9, -9])
lst[1] = 4
print("合計：{}".format(lst.sum_plus_value()))
lst.remove_minus_value()
print(lst)
