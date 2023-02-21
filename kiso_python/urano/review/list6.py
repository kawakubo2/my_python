list6 = ['A', 'C', 'B', 'X', 'Y', 'A', 'X', 'C', 'A']

c = input('英字1文字: ')

counter = 0
for elem in list6:
    if c == elem:
        counter += 1
if counter > 0:
    print(f"{c}は{counter}個あります")
else:
    print(f"{c}は存在しません。")