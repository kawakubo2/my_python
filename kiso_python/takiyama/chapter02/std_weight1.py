height = float(input("身長を入力してください(cm): "))
bmi = 22
std_weight = bmi * (height / 100) ** 2
print("身長: " + str(height) + "cm → ", end = "")
# 1
print("標準体重: " + str(std_weight) + "kg")
# 2
print("標準体重%.2fkg" % (std_weight))
# 3
print("標準体重{:.2f}kg".format(std_weight))
# 4
print(f"標準体重{std_weight:.2f}kg")

name = "山田太郎"
age = 42

print(name + "さんの年齢は" + str(age) + "歳です。")
print(f"{name}さんの年齢は{age}歳です。")
