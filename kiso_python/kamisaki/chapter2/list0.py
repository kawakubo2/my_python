numbers = [30, 38, 27, 50, 69, 70, 35]

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# print(numbers[5])
# print(numbers[6])
for n in numbers:
    print(str(n) + ' ', end='')
print()

for i in range(len(numbers) - 1, -1, -1):
    print(str(numbers[i]) + ' ', end='')
print()

for n in reversed(numbers):
    print(str(n) + ' ', end='')
print()

for i in range(-1, -8, -1):
    print(str(numbers[i]) + ' ', end='')
print()

numbers.append(12)
print(numbers)
numbers[7] = 20
print(numbers)
x = numbers.pop(1)
print('取り出した値:', x)
print(numbers)

tuple_numbers = 3, 1, 10, 7, 8, 5, 9
print(tuple_numbers)

list_numbers = list(tuple_numbers)
print(list_numbers)

s = "日月火水木金土"
print(s[2])
for c in s:
    print(c + '曜日')

subject = 'understanding the linux kernel'
print(subject.title())

print(id(12))
print(id(3 * 4))

n = 12
print(id(n))

