# -*- coding: utf-8 -*-

def twice(n):
    n *= 2
    return n
    
x = 10
x = twice(x)

print('x = ', x)

# =============================================================================
def twice_array(nums):
    for i in range(len(nums)):
        nums[i] *= 2
# =============================================================================
        
# =============================================================================
# def twice_array(nums):
#     for n in nums:
#         n *= 2
# =============================================================================
        
numbers = [1, 2, 3, 4, 5]

twice_array(numbers)

print(numbers)

print(1, 2, 3, 4, 5, 6, sep='@', end='\n\n')
print(100)

def triangle(base = 1, height = 1):
    return base * height / 2

print(triangle())


print(triangle(height = 30, base = 40))

print('a', 'b', 'c')

# parameter ---> 仮引数、パラメータ
# argument  ---> 実引数,引数

def change(price, put_price, currency_symbol = '￥'):
    return currency_symbol + str(put_price - price)
    
p1 = 1000
p2 = 300
print(change(p2, p1, '$'))
    