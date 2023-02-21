colors = ['赤', '青', '黄', 'オレンジ']

try:
    print(colors[4])
except:
    print("インデックス外")

print(colors[3])
print(colors[-1])
print(colors[len(colors) - 1])

try:
    print(colors[len(colors)])
except:
    print("インデックス外")