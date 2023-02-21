import math
def myceil(num, keta):
    return math.ceil(num * math.pow(10, keta)) / math.pow(10, keta)
def myfloor(num, keta):
    return math.floor(num * math.pow(10, keta)) / math.pow(10, keta)

# 高階関数(higher order function)
def higher_round(func, num, keta): 
    return func(num * math.pow(10, keta)) / math.pow(10, keta)

print(higher_round(math.ceil, 123.4567, 2))
print(higher_round(math.floor, 123.4567, 2))

n = 123456789

print(higher_round(math.floor, n, -3))

kuji = ['大吉', '中吉', '凶']
import random
print(random.choice(kuji))

m = 10
m = m + 1
m += 1

drink = 2

if drink == 1:
    print('コーヒー')
elif drink == 2:
    print('オレンジジュース')
elif drink == 3:
    print('緑茶')

"""
switch(drink):
    case 1:
        print('コーヒー')
        break
    case 2:
        print('オレンジジュース')
        break
    case 3:
        print('緑茶')
        break
}
liquor = '焼酎'
switch(liquor):
    case 'ウィスキー':
    case '焼酎':
    case 'ブランデー':
        print('蒸留酒');
        break;
    case 'ビール':
    case '日本酒':
        print('醸造酒')
        break;
}
"""

"""
for (let i = 0; i < numbers.length; i++) {
    print(numbers[i]);
}
"""

a = 10
def nibai(n):
    n *= 2 # n = n * 2

nibai(a)
print(a)

numbers = [1, 2, 3]
def nibai2(nums):
    """
    for n in nums:
        n *= 2
    """
    for i in range(len(nums)):
        nums[i] *= 2    

nibai2(numbers)

print(numbers)
