data = [['あ', 'い']] * 3
print(data)
data[0].append('う')
print(data)

data2 = ['あ', 'い'] * 3
print(data2)
data2[0] = 'う'
print(data2)

data3 = ['a', 'b', 'c']
data4 = ['d', 'e']

data5 = data3 + data4
print(data3)
print(data4)
print(data5)

data3.extend(data4)
print(data3)

result = []
data6 = [[1, 2, 3],[4, 5],[6, 7, 8, 9]]
for lst in data6:
    result.extend(lst)

print(data6)
print(result)

data7 = ['ぱんだ', 'うさぎ', 'こあら', 'とら']
data8 = sorted(data7)
print(data8)
print(data7)