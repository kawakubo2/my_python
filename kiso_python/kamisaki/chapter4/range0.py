for n in range(10):
    print(f"{n} ", end="")
print()

for n in range(0, 21, 2):
    print(f"{n} ", end="")
print()

result = []
for num in range(0, 21, 2):
    result.append(num ** 2)
print(result)

print([num ** 2 for num in range(0, 21, 2)])

numbers = [88, 72, 68, 82, 77, 92, 80, 75, 98, 70]
avg = sum(numbers) / len(numbers)
variant = sum([(num - avg) ** 2 for num in numbers]) / len(numbers)
print(f"分散: {variant}")
print(f"標準偏差: {variant ** 0.5}")