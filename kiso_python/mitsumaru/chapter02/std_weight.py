height = float(input("身長(cm)を入力してください: "))
bmi = 22
std_weight = bmi * (height / 100) ** 2
print("身長: " + str(height) + "cm → ", end="")
print("標準体重: " + str(std_weight) + "kg")