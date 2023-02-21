list41 = [
    '5,12,3', '10,8,6', '11,2,3', '9,7,5'
]

# 20
# 24
# 16
# 21

for nums in list41:
    total = 0
    for n in nums.split(','):
        total += int(n)
    print(total)