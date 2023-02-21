# -*- coding: utf-8 -*-

def average(*nums):
    if len(nums) == 0:
        print(nums)
        return 0
    return sum(nums) / len(nums)


print(average(1, 10, 100))
print(average())


numbers = [8, 7, 11, 22, 4, 5, 13]

print('合計:', sum(numbers))
print('平均:', sum(numbers) / len(numbers))
print('最大:', max(numbers))
print('最小:', min(numbers))

def func(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)
    
func(1, 2, 3, 4, 5, height = 172, weight = 90)
func("abc", 1, 2, 3, 4, name = "山田太郎", age = 30)
