from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_square_total = reduce(lambda total, n: total + n, map(lambda n: n**2, filter(lambda n: n % 2 == 0, numbers)))
print(even_square_total)

even_square_total2 = sum([n ** 2 for n in numbers if n % 2 == 0])
print(even_square_total2)