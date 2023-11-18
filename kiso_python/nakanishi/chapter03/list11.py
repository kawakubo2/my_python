numbers = [1, 2, 3, 4, 5]

def jubai(nums):
    for n in nums:
        n *= 10

jubai(numbers)
print(numbers)

def jubai2(nums):
    for i in range(len(nums)):
        nums[i] *= 10

jubai2(numbers)
print(numbers)