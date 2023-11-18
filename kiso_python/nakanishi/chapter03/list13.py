numbers1 = list(range(0, 101, 10))
print(numbers1)

numbers2 = []
for n in range(0, 101, 10):
    numbers2.append(n)
print(numbers2)

# リストの内包表記
numbers3 = [n for n in range(0, 101, 10)]
print(numbers3)