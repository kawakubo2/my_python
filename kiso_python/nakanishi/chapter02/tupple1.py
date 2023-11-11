height = (180, 165, 159, 171, 155)
# できること
# インデックスを指定した要素の取得
print(height[2])
# 要素数の取得
print(len(height))
# for文で回す
for h in height:
    print(h)

# できないこと
# 要素の変更
# height[1] = 177 # 'tuple' object does not support item assignment・・・要素の変更は不可
# print(height[1])
# height.append(177);
