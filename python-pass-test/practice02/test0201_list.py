# -*- coding: utf-8 -*-
def print_array(nums):
    for n in nums:
        print("{} ".format(n), end="")
    print()

numbers = [8, 5, 3, 9, 11, 7]

print_array(numbers)

size = len(numbers)

index = 0;
while index < (size // 2):
    temp = numbers[size - index - 1]
    numbers[size - index - 1] = numbers[index]
    numbers[index] = temp
    index += 1
    
print_array(numbers)



