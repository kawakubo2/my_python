members = [
    {'name': '山田太郎', 'weight': 72, 'height': 170},
    {'name': '田中一郎', 'weight': 72, 'height': 165},
    {'name': '鈴木次郎', 'weight': 72, 'height': 180},
    {'name': '佐藤勝男', 'weight': 72, 'height': 172},
]

def bmi(weight, height):
    return weight / (height / 100) ** 2

name_bmi = [(m['name'], bmi(m['weight'], m['height'])) for m in members]
print(name_bmi)
name_bmi1 = sorted(name_bmi, key=lambda e: e[1], reverse=True)
print(name_bmi1)