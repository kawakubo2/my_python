numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

numbers[4] = 100

numbers.append(60)

print('後ろの方から指定する')

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5])
print(numbers[-6])

print(len(numbers))
print('for文により取り出し')
for n in numbers:
    print(n)