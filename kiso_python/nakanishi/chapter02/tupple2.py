t1 = ("赤", "黒", "緑")

l1 = list(t1)
print(l1)
l1.append("青") # リストはappendメソッドを持っている
print(l1)

print(t1)

t2 = tuple(l1)
print(t2)

s1 = "ABCDEFG"
for c in s1:
    print(c)
print('--- index(添え字)でアクセス可能 ---')
print(s1[0])
print(s1[1])
print(s1[2])
print(s1[3])
print(s1[4])
print(s1[5])
print(s1[6])

# num1 = 12345
# print(num1[0])

# リスト、タプル、文字列をシーケンス型と呼ぶ

s2 = "日月火水木金土"
for c in s2:
    print(c + "曜日")

s3 = "Python"
s4 = s3.upper()
print(s4)
print(s3 == s4)
print(s3)