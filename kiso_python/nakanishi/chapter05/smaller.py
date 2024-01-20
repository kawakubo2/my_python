def smaller1(num1, num2):
    return num2 if num1 > num2 else num1

print(smaller1(9, 2))
print(smaller1(1, 11))

smaller2 = lambda num1, num2: num2 if num1 > num2 else num1

print(smaller2(9, 2))
print(smaller2(1, 11))
