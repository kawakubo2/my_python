# recursive_func1.py

numbers = [1, [2, 3, [4, 5], [6, 7]], [8, 9], 10]

def array_sum(nums):
    if type(nums) != list:
        raise Exception("引数がリストではない")
    total = 0
    for n in nums:
        if type(n) == list:
            total += array_sum(n)
        else:
            total += n
    return total

total = array_sum(numbers)
print(f"合計: {total}")