# -*- coding: utf-8 -*-
#
# 奇数桁はそのまま合計に加算
# 偶数桁は3倍して合計に加算
#
#　10から合計を10で割った余りを引く
# 
#
def check_digit(isbn):
    total = 0
    isbn = isbn.replace('-', '')[0:-1]
    for index, d in enumerate(isbn):
        num = int(d)
        if index % 2 == 0:
            total += num
        else:
            total += num * 3
    remainder = total % 10
    if remainder == 0:
        return 0
    else:
        return 10 - remainder
        

isbns = ['978-4-8443-8015-3', '978-4-7980-4127-8', '978-4-87311-730-0']

for isbn in isbns:
    print('isbn: {} check_digit: {}'.format(isbn, check_digit(isbn)))
    