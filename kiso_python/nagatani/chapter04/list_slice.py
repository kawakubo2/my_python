print('---< 置換え >--')
s = ["A", "B", "C", "D", "E", "F", "G", "H"]
s[2:5] = ["X", "Y"]
print(s)

print('---< 挿入 >---')
s = ["A", "B", "C", "D", "E", "F", "G", "H"]
s[2:2] = ["X", "Y", "Z"]
print(s)

print('---< 削除 >---')
s = ["A", "B", "C", "D", "E", "F", "G", "H"]
s[2:5] = []
print(s)

s2 = "東京,大坂,名古屋,京都,青森"
lst = s2.split(',')
print(lst)
s3 = "-".join(lst)
print(s3)

lst.append("福岡")
print(lst)
print(lst.pop(0))
print(lst)