# -*- coding: utf-8 -*-

def func(**dic):
    print(dic)
    
func(name="田中一郎", num=1)
func(name="山田太郎", age=59, num=2, point=60)

def func1(**dic):
    for key, value in dic.items():
        print("{}:{}".format(key, value))
        
func1(name="田中一郎", num=1)
func1(name="山田太郎", age=59, num=2, point=60)

def smaller(num1, num2):
    return num2 if num1 > num2 else num1

print(smaller(9, 2))
print(smaller(1, 11))

smaller2 = lambda num1, num2: num2 if num1 > num2 else num1

print(smaller2(9, 2))
print(smaller2(1, 11))
        