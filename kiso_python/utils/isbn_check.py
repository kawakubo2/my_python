def isbn_check(isbn):
    total = 0
    isbn = isbn.replace('-', '')[0:-1]
    for i, n in enumerate(isbn):
        n = int(n)
        total += n if i % 2 == 0 else n * 3
    return 10 - (10 if total % 10 == 0 else total % 10)

isbns = ['978-4-7741-5377-3',
         '978-4-7980-5347-9',
         '978-4-7981-4461-0']

for isbn in isbns:
    print('isbn={}, actual={}, expected={}'.format(\
          isbn, isbn_check(isbn), isbn[-1]))
    