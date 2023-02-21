employees = {
    "A101": {"name": "山田太郎", "age": 38, "weight": 78, "height": 170},
    "A102": {"name": "横山花子", "age": 28, "weight": 55, "height": 160},
    "B103": {"name": "田中一郎", "age": 45, "weight": 83, "height": 180},
}

while True:
    number = input("社員番号(終了時はq): ")
    if number == "q":
        break
    if number in employees:
        employee = employees[number]
        print(f"名前: {employee['name']} 年齢: {employee['age']}")
    else:
        print(f"{number}に該当する社員は存在しません")