import sys

# print(sys.argv)
total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])

print(f'合計: {total}')

numbers = [1, 2, 3, 4, 5, 6]
print(sum(numbers))