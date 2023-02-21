# -*- coding: utf-8 -*-

numerator = [ 100, 200, 300, 400, 500]
denominator = [5, 4, 0, 2, 1]

errors = []

for i, (n, d) in enumerate(zip(numerator, denominator)):
    try:
        print(n / d)
        print('aaaaaa')
        
        print('zzzzzz')
    except ZeroDivisionError:
        print('0除算発生 分子:{} 分母:{}'.format(n, d))
        errors.append((i, n))
        
print(errors)


        