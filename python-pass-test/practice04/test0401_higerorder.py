# -*- coding: utf-8 -*-

def my_filter(numbers, func):
    result = []
    for n in numbers:
        if (func(n)):
            result.append(n)
    return result

def print_array(numbers):
    for n in numbers:
        print("{} ".format(n), end="")
    print()
    
numbers = [8, 5, 3, -4, 7, -1, 4, 6, 9]

print_array(numbers)

even_numbers = my_filter(numbers, lambda n: n % 2 == 0)
print_array(even_numbers)