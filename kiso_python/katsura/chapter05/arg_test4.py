def test3(lst):
    lst = lst + [3, 4]
    return lst

list1 = [1, 2, 3]
list2 = test3(list1)
print(list2)