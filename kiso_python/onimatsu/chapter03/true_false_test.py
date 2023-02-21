# -*- coding: utf-8 -*-

n1 = 3
n2 = 0
str1 = 'abc'
str2 = ''
list1 = [1, 2, 3]
list2 = []

def true_or_false(value):
    print(str(value) + 'は', end='')
    if value:
        print('True', end='')
    else:
        print('False', end='')
    print('とみなされる')

true_or_false(n1)
true_or_false(n2)
true_or_false(str1)
true_or_false(str2)
true_or_false(list1)
true_or_false(list2)


    