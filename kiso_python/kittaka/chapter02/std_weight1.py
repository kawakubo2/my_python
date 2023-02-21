# std_weight1.py
height = float(input("身長(cm): "))
bmi = 22

std_weight = 22 * (height / 100) ** 2
print("身長: " + str(height) + "cm → ", end="")
print("標準体重: " + "\033[31m" + str(std_weight) + "\033[0mkg")
print("\a肥満気味です。")