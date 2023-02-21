members = [
    {'name': '山田太郎', 'weight': 70, 'height': 178},
    {'name': '田中一郎', 'weight': 70, 'height': 173},
    {'name': '鈴木次郎', 'weight': 70, 'height': 175},
    {'name': '佐藤勝男', 'weight': 70, 'height': 176},
]

def bmi(weight, height):
    return weight / (height / 100) ** 2

members.sort(key=lambda m: bmi(m['weight'], m['height']))

print(members)