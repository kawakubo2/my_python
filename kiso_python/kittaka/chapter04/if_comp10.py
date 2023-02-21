employees = [
    {"name": "山田太郎", "weight": 72, "height": 170},
    {"name": "横山花子", "weight": 55, "height": 150},
    {"name": "田中一郎", "weight": 88, "height": 177},
    {"name": "鈴木次郎", "weight": 80, "height": 172},   
]

def bmi(weight, height):
    return weight / (height / 100) ** 2

rechecked_employees = [e['name'] for e in employees if bmi(e['weight'], e['height']) >= 27]
print(rechecked_employees)