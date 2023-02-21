name = '山田太郎';
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# シーケンス型　---> 文字列型, リスト型, タプル型

height = [180, 165, 159, 167, 178]
print(height[0])
print(height[1])
print(height[2])
print(height[3])
print(height[4])

print('要素数:' + str(len(height)))

height[0] = 182

height.append(195)

for h in height:
    print(h)

height.pop()
for h in height:
    print(h)

t1 = ('赤', '黒', '緑')
l1 = list(t1)
l1.append('黄色');
print(l1)
print(t1)

n = 123
print(id(n))
m = 123
print(id(m))
print(id('赤'))
