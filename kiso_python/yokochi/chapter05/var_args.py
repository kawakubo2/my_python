print(1, 2, 3, 4, 5, 6)
print()

def total(*nums):
    result = 0
    for n in nums:
        result += n
    return result

print(total())
print(total(1))
print(total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))