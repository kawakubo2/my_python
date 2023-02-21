s = "0123456789"
print(s[1:5])

s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0,len(s2),5):
    if i + 5 < len(s2):
        end = i + 5
    else:
        end = len(s2)
    print(s2[i:end])
print('-------------')
print(s2[0:5])
print(s2[5:10])
print(s2[10:15])
print(s2[15:20])
print(s2[20:25])
print(s2[25:26])

s3 = "Python"
print(s3 * 10)

# formatメソッド
name = "山田太郎"
age = 38
print(name + "さんの年齢は" + str(age) + "歳です。")
print("%sさんの年齢は%d歳です。" % (name, age))
print("{}さんの年齢は{}歳です。".format(name, age))
print(f"{name}さんの年齢は{age}歳です。")