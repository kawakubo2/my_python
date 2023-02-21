# -*- coding: utf-8 -*-

lst = [num ** 2 for num in range(0, 21, 2)]

print(lst)

lst2 = [6, 4, 3, 7, 5, 5, 4, 6, 5, 5]
avg = sum(lst2) / len(lst2)

std = (sum([(num - avg) ** 2 for num in lst2]) / len(lst2)) ** 0.5

print(lst2)
print("標準偏差: {:.2f}".format(std))