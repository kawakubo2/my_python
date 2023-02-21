# func2.py

def total(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"合計: {total(numbers)}")