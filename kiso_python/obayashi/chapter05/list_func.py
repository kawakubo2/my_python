numbers = [1, 2, 3, 4, 5]

def nibai(nums):
    for i in range(len(nums)):
        nums[i] *= 2 # nums[2] ---> *(num + 2)
    nums.append(100)
    """
    for n in nums:
        n *= 2
    """
        
nibai(numbers)
print(numbers)