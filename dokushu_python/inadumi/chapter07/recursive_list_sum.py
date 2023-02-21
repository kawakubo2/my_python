numbers = [1, [2, 3, [4, 5], 6], [7 ,[8, 9]], 10]

def recursive_list_sum(nums):
    if type(nums) != list:
        raise ValueError(f'リストではない')

    total = 0
    for n in nums:
        if type(n) == list:
            total += recursive_list_sum(n)
        else:
            total += n

    return total

print(f'合計: {recursive_list_sum(numbers)}')