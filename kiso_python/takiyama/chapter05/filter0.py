numbers = [-3, 4, 2, 9, 7, 8, -4, 3]

for even in filter(lambda n: n % 2 == 0, numbers):
    print(even)

for minus in filter(lambda x: x < 0, numbers):
    print(minus)