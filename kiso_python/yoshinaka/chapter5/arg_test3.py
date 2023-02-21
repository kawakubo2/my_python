def double(num):
    num *=  2
    return num

n = 5
n = double(n)
print(n)

def double_array(nums):
    for i in range(len(nums)):
        nums[i] *= 2

numbers = [1, 2, 3, 4, 5]
print('double_array呼び出し前:', numbers)
double_array(numbers)
print('double_array呼び出し後:', numbers)