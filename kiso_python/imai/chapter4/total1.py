# -*- coding: utf-8 -*-

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 120



total = 1
for n in range(1, 6):
    total *= n
    
print(total)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
    