# -*- coding: utf-8 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(numbers)
print('total=' + str(total))

def add(x, y):
    return x + y

answer = add(10, 20)

print('合計:' + str(answer))

abc = add

print(abc(100,200))

add = 'abc'

# answer = add(10, 20)

def sum(a, b):
    return a * b

print(sum(5, 4))

"""
静的型付け言語　--- 一度型を決めたら変更できない
C, C++, C#, Java

動的型付け言語 --- 変数に型の制約がない
Python, JavaScript, PHP
"""