def nibai(lst):
    for i in range(len(lst)):
        lst[i] *= 2

nums = [1, 2, 3, 4, 5]
print(f"呼び出し前: {nums}")

nibai(nums)
print(f"呼び出し後: {nums}")
