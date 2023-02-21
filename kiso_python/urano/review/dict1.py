colors = {'赤': 'Red', '青': 'Blue', '緑': 'Green'}

print(colors['青'])

# 赤=>Red
# 青=>Blue
# 緑=>Green

for en, ja in colors.items():
    print(f"{en}=>{ja}")

print('---黒を追加---')
colors['黒'] = 'Black'
for en, ja in colors.items():
    print(f"{en}=>{ja}")

# 0(日),1(月)・・・6(土)
def youbi(num):
    w = ['日', '月', '火', '水', '木', '金', '土']
    if num < 0 or num >= len(w):
        return None
    return w[num]

print(youbi(0))
print(youbi(1))
print(youbi(2))
print(youbi(3))
print(youbi(4))
print(youbi(5))
print(youbi(6))
    