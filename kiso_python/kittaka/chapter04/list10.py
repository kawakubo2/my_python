numbers = [
    "1,2,3,4,5",
    "6,7,8,9,10",
    "11,12,13,14,15"
]

total = 0
for nums_str in numbers:
    nums = nums_str.split(',')
    sub_total = 0
    for n_str in nums:
        sub_total += int(n_str)
    print(sub_total)
    total += sub_total
print('----')
print(total)
    