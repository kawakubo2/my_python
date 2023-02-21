def test1(num):
    num += 10
    print(f"num={num}")

n = 3
test1(n)
print(f"n={n}")

def test2(nums):
    nums[0] = 100

numbers = [1, 2, 3, 4, 5]
test2(numbers)
print(numbers)

def test3(nums):
    for i in range(len(nums)):
        nums[i] += 10

test3(numbers)
print(numbers)