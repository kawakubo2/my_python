list44 = [
    ["山田太郎", 77, 90, 88], ["横山花子", 80, 70, 82], ["田中一郎", 90, 88, 92]
]

# 山田太郎 255
# 横山花子 232
# 田中一郎 270

for student in list44:
    name, kokugo, sugaku, eigo = student
    print(f"{name}: {int(kokugo)+int(sugaku)+int(eigo)}")