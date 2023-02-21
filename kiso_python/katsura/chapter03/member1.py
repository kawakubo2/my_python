import sys

members = ['A01', 'B02', 'A03', 'A04', 'B03', 'C01']

member = 'B03'

isexists = False
for m in members:
    if m == member:
        isexists = True
        break

if isexists:
    print(f"{member}は名簿にあります。")
else:
    print(f"{member}は名簿に見つかりません。")

for m in members:
    if m == members:
        break
else:
    print(f"{member}は名簿に見つかりません。")
    sys.exit()
    
"""
名簿に見つかった時の処理
"""