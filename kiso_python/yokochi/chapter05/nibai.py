def nibai(n):
    n *= 2

m = 10
nibai(m)
print(m)

def nibai_list(nums):
    for i in range(len(nums)):
        nums[i] *= 2

def nibai_list_ng(nums):
    for n in nums:
        n *= 2

numbers = [1, 2, 3]
nibai_list(numbers)
print(numbers)

numbers = [1, 2, 3]
nibai_list_ng(numbers)
print(numbers)