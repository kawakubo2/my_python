members = [
    {'name': '山田太郎', 'weight': 70, 'height': 168},
    {'name': '田中一郎', 'weight': 70, 'height': 180},
    {'name': '鈴木次郎', 'weight': 70, 'height': 172},
    {'name': '佐藤勝男', 'weight': 70, 'height': 165},
]

def bmi(member):
    return member['weight'] / (member['height'] / 100) ** 2

members.sort(key=bmi)
print(members)