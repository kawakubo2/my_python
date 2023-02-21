a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

b = a[::-1]
print(f"元のa{a}")
print(f"aを反転{b}")
print(F"aは変化しない{a}")

a.reverse()
print(a)
a.reverse()
print(a)

a.append('J')
print(a) 
e = a.pop()
print(f"最後の要素{e}を削除")
print(a)
e = a.pop(3)
print(f"3番目の要素{e}を削除")
print(a)
e = a.pop(0)
print(f"先頭の要素{e}を削除")
print(a)
a.remove('F')
print('Fを削除')
print(a)
del a[2:4]
print('2番目と3番目を削除')
print(a)

b = ['A', 'B', 'C', 'A', 'D', 'A']
# c = [c for c in b if c != 'A']
while 'A' in b:
    b.remove('A')
print(b)
