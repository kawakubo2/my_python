data1 = [1, 3, 5]
data2 = [2, 7, 8]

result = map(lambda v1, v2: v1 * v2, data1, data2)

print(list(result))

avg1 = sum(data1) / len(data1)
avg2 = sum(data2) / len(data2)

prod = map(lambda v1, v2: (v1 - avg1) * (v2 - avg2), data1, data2)
coeff = sum(list(prod)) / len(data1)
print(coeff)