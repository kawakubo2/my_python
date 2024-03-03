numbers = [1, 2, 3, 4, 5]
numbers2 = numbers[-1::-1]
print(numbers2)
print(numbers == numbers2)

numbers3 = reversed(numbers)
for n in numbers3:
    print(f"{n} ", end="")
print()
print(numbers)