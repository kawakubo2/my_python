list18 = [
    [5, 2],
    [4, 3],
    [8, 5],
    [4, 5],
    [7, 4]
]

# 10 12 40 20 28
total = 0
for rect in list18:
    total += rect[0] * rect[1]
    print(f"{rect[0] * rect[1]:4}", end="")
print(f"{total:4}")