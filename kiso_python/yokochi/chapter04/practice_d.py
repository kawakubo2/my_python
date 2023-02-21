customers = [('田中一郎', 25), ('山田太郎', 23), ('佐藤花子', 15),
             ('猫山五郎', 33), ('小林直子', 26), ('大木虎夫', 18)]

names = [n[0] for n in customers if n[1] >= 20]
print(names)

members = [
    {'name': '山田太郎', 'weight': 60, 'height': 175},
    {'name': '田中一郎', 'weight': 60, 'height': 168},
    {'name': '鈴木次郎', 'weight': 88, 'height': 180},
    {'name': '佐藤勝男', 'weight': 80, 'height': 158},
];

def bmi(weight, height):
    return weight / (height / 100) ** 2

names = [member['name'] for member in members if bmi(member['weight'], member['height']) > 25]
print(names)