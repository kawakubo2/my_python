# -*- coding: utf-8 -*-

numbers = [ 70, 82, 75, 90, 98, 67, 88, 92, 93, 83 ]

avg = sum(numbers) / len(numbers)

var1 = sum([(avg - n) ** 2 for n in numbers]) / len(numbers)

print("平均: {:.2f}  分散: {:.2f}  標準偏差: {:.2f}".format(avg, var1, var1 ** 0.5))