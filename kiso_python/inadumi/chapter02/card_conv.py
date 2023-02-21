# -*- coding: utf-8 -*-

digit_chars = "0123456789ABCDEF"

n = 891
lst = []

while n > 0:
    remainder = n % 16
    lst.append(digit_chars[remainder])
    n //= 16
    
lst.reverse()
num = ''.join(lst)
print(num)