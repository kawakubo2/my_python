# リストの内包表記

# 内包表記を使わない方法

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

result = []
for n in numbers:
    if n > 0 and n % 2 == 0:
        result.append(n)

print(result)

# 内包表記を使う方法
result2 = [n for n in numbers if n > 0 and n % 2 == 0]
print(result2)