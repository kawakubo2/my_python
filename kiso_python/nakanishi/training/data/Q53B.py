def calc_price(gender, age):
    if gender not in ("M", "F"):
        raise ValueError("性別はMまたはFで入力してください")
    if type(age) != int or age < 0:
        raise ValueError("年齢は0以上の整数値を入力してください")
    
    price = 0
    if gender == "F":
        if age <= 20:
            price = 2200
        elif age <= 50:
            price = 2400
        elif age <= 70:
            price = 2600
        else:
            price = 2800
    else:
        if age <= 20:
            price = 2400
        elif age <= 50:
            price = 2800
        elif age <= 70:
            price = 3200
        else:
            price = 3600
    return price
        
data = [
    {"gender": "M", "age": 15, "expected": 2400},
    {"gender": "M", "age": 20, "expected": 2400},
    {"gender": "M", "age": 38, "expected": 2800},
    {"gender": "M", "age": 50, "expected": 2800},
    {"gender": "M", "age": 63, "expected": 3200},
    {"gender": "M", "age": 70, "expected": 3200},
    {"gender": "M", "age": 75, "expected": 3600},
    {"gender": "M", "age": 18, "expected": 2200},
    {"gender": "F", "age": 20, "expected": 2200},
    {"gender": "F", "age": 41, "expected": 2400},
    {"gender": "F", "age": 50, "expected": 2400},
    {"gender": "F", "age": 59, "expected": 2600},
    {"gender": "F", "age": 70, "expected": 2600},
    {"gender": "F", "age": 88, "expected": 2800},
]
try:
    for item in data:
        print(f"""性別: {'男性' if item['gender'] == 'M' else '女性'} 
年齢: {item['age']} 期待値: {item['expected']} 検出値: {calc_price(item['gender'], item['age'])}
{'○' if item['expected'] == calc_price(item['gender'], item['age']) else '×'}""")
except ValueError as e:
    print(e)
    
        