list42 = [
    '山田太郎,88,70,55', '横山花子,72,68,90', '田中一郎,90,88,92'
]

# 山田太郎 213
# 横山花子 230
# 田中一郎 270

for student in list42:
    name, kokugo, sugaku, eigo = student.split(',')
    print(f"{name} {int(kokugo)+int(sugaku)+int(eigo)}")