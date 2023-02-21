students = [
    ["山田太郎", 28, 170, 72],
    ["山田花子", 32, 158, 50],
    ["田中一郎", 39, 178, 78]
]

for student in students:
    name,age,height,weight = student
    bmi = weight / (height/100) ** 2
    print(f"{name}({age})さんのBMI値は{bmi:.1f}")
    bmi = student[3] / (student[2] / 100) ** 2
    print(f"{student[0]}({student[1]})さんのBMI値は{bmi:.1f}")