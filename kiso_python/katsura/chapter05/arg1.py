def nibai(n):
    n *= 2

m = 10
nibai(m)
print(m)

def list_nibai(nums):
    for n in nums:
        n *= 2
    # for i in range(len(nums)):
    #     nums[i] *= 2

numbers = [1, 2, 3]
list_nibai(numbers)
print(numbers)