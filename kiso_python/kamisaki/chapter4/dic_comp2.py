e_seasons = ["Spring", "Summer", "Autumn", "Winter"]
j_seasons = ["春", "夏", "秋", "冬"]

seasons = {e:j for e, j in zip(e_seasons, j_seasons)}
print(seasons)

seasons2 = {j:e for e, j in zip(e_seasons, j_seasons)}
print(seasons2)

list1 = ['サンマ', 'ダイコン', 'キュウリ', 'ギュウニク', 'カツオ']
list2 = ['魚', '野菜', '野菜', '肉', '魚']

shokuzai1 = {a:b for a, b in zip(list1, list2)}
print(shokuzai1)
shokuzai2 = {b:a for a, b in zip(list1, list2)}
print(shokuzai2)

tensor = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18],
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

flat = [x for matrix in tensor for row in matrix for x in row]

print(flat)

flat2 = []
for matrix in tensor:
    for row in matrix:
        for x in row:
            flat2.append(x)

print(flat2)