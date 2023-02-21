def test1(num):
    num += 10

n = 3
test1(n)
print(n)

def nibai(nums):
    for i in range(len(nums)):
        nums[i] *= 2

numbers = [10, 20, 30, 40, 50]
nibai(numbers)
print(numbers)