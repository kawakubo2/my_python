# 関数定義
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

a = 10
b = 20
print(str(a) + "+" + str(b) + "=" + str(add(a, b)))
print(f"{a}+{b}={add(a,b)}")

numbers = [1, 2, 3, 4, 5, 6, 7]

def list_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

answer = list_sum(numbers)
print("合計: {}".format(answer))

numbers2 = [21, 18, 7, 38, 29, 51, 33, 60, 2, 11]


def list_max(nums):
    if len(nums) == 0:
        raise ValueError("リストが空")
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def list_min(nums):
    if len(nums) == 0:
        raise ValueError("リストが空")
    min = nums[0]
    for n in nums:
        if n < min:
            min = n
    return min


my_max = list_max(numbers2)
print(f"最大値: {my_max}")
my_min = list_min(numbers2)
print(f"最小値: {my_min}")

a = (2, 3)
b = (6, 6) 

from math import pow, sqrt

def distance(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

print(f"距離: {distance(a, b)}")