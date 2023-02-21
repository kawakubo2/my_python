# -*- coding: utf-8 -*-

def even_filter(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

def print_array(numbers):
    for n in numbers:
        print("{} ".format(n), end="")
    print()

numbers = [-5, 8, -3, -4, 7, 6, 4, -2]

print("---< フィルタリング前 >---")
print_array(numbers)

even_numbers = even_filter(numbers)

print("---< フィルタリング後 >---")
print_array(even_numbers)