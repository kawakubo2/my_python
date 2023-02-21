fruits = ['バナナ', 'りんご', 'なし', 'ぶどう', 'オレンジ']
fruits.append('パイナップル') # リストの末尾に追加
fruits[1] = 'いちご' # リストの内容の変更

fruit = fruits.pop() # リストの末尾から削除
print(f"{fruit}を末尾から削除しました。")

print(fruits[1:3])

for f in fruits:
    print(f)

numbers = [ 9, 12, 5, 3, 8, 7, 10, 18, 2, 6 ]

total = 0
for n in numbers:
    # total = total + n
    total += n
    
print(f"合計: {total}")