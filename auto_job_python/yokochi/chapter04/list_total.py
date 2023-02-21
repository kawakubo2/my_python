numbers = [1, [2, 3, [4, 5], [6, 7]], [8, 9], 10]

def list_total(nums):
    total = 0
    for n in nums:
        if type(n) == list:
            total += list_total(n)
        else:
            total += n
    return total

print(f"合計: {list_total(numbers)}")