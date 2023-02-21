import sys

numbers = [ 82, 12, 38, 93, 39, 25, 70, 48, 52, 29 ]

size = len(numbers)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        k = (size - 1) - j
        if k <= i: break
        if numbers[k - 1] > numbers[k]:
            temp = numbers[k]
            numbers[k] = numbers[k - 1]
            numbers[k - 1] = temp

for n in numbers:
    print(n)

print('---< 2分探索 >---')
def binary_search(array, n):
    left = 0
    right = len(array) - 1
    while (left <= right):
        mid = (left + right) // 2
        if n > array[mid]:
            left = mid + 1
        elif n < array[mid]:
            right = mid - 1
        else:
            return True
    else:
        return False 

for n in range(101):
    if binary_search(numbers, n):
        print(n)