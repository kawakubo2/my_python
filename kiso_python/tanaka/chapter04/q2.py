fruits = [("バナナ", 5),("オレンジ", 3),("イチゴ", 10),("バナナ", 8),("バナナ", 7),
          ("オレンジ", 9),("イチゴ", 8)]

counter = {}
for fruit in fruits:
    if fruit[0] in counter:
        counter[fruit[0]] += fruit[1]
    else:
        counter[fruit[0]] = fruit[1]

for fruit, num in counter.items():
    print(f"{fruit}: {num}")