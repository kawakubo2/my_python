lst = []
lst.append("春")
lst.append(["夏","秋", "冬"])
print(lst) # ["春", ["夏", "秋", "冬"]]

print(lst[0])
print(lst[1][0])
print(lst[1][1])
print(lst[1][2])

lst2 = []
lst2.append("春")
lst2 += ["夏", "秋", "冬"]
print(lst2)

salaries = [50, 
                [40, 
                    [25, 18, 30, 40]
                ], 
                [42, 
                    [20, 33, 38, 18, 18]
                ]
           ]

salaries = [50, 40, 25, 18, 30, 40, 42, 20, 33, 38, 18, 18]

total = 0
for s in salaries:
    total += s # total = total + s
print(f'部の給与合計: {total}')

print(f'部の給与合計: {sum(salaries)}')