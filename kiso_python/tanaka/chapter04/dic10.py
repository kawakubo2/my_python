fruits = [
    {'バナナ': 10, 'リンゴ': 5, 'イチゴ': 3},
    {'ブドウ': 7, 'リンゴ': 3, 'バナナ': 3},
    {'リンゴ': 4, 'ブドウ': 2, 'イチゴ': 4}
]

result = {}

for daily_sales in fruits:
    for fruit, num in daily_sales.items():
        if fruit in result:
            result[fruit] += num # result[fruit] = result[fruit] + num
        else:
            result[fruit] = num
            
print(result)