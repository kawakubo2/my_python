a = 10
b = 3

print(a / b)
print("%.1f" % (a / b))
print("{:.1f}".format(a / b))
print(f"{a / b:.1f}")

name = "山田太郎"
age = 38
print("%sさんの年齢は%d歳です。" % (name, age))
print("{}さんの年齢は{}歳です。".format(name, age))
print(f"{name}さんの年齢は{age}歳です。")

name1 = "山田太郎"
name2 = "横山花子"

print("{1}さん。私は{0}です。...あれ、{1}さんですよね".format(name1, name2))