smaller = lambda num1, num2: num2 if num1 > num2 else num1

print(smaller(55, 232))
print(smaller(-32, -8))

my_min = smaller
print(my_min(1, 101))