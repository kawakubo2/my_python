colors1 = ['yellow', 'red', 'green']
colors2 = ['黄色', '赤', 'green']
# リストの内包表記
max_length = max([len(c) for c in colors1])
for en, ja in zip(colors1, colors2):
    print(f"{en} : {ja}")