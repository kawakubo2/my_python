members = [
    {'name': '山田太郎', 'weight': 70, 'height': 170},
    {'name': '田中一郎', 'weight': 70, 'height': 165},
    {'name': '鈴木次郎', 'weight': 70, 'height': 180},
    {'name': '佐藤勝男', 'weight': 70, 'height': 168},
]

def bmi(member):
    return member['weight'] / (member['height'] / 100) ** 2

for member in sorted(members, key=bmi):
    print(member)