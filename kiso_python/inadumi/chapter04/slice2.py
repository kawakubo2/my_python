# -*- coding: utf-8 -*-

numbers = [1, 2, 3, 4, 5, 6, 7]

# numbersはそのままで、逆順になったリストを返す(非破壊的)
r_numbers = numbers[::-1]
print(r_numbers)

# 元の配列の並び順を変える(破壊的)
numbers.reverse()
print(numbers)