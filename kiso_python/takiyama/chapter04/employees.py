employees = {
    1001: {"name": "山田太郎", "address": "山形県天童市", "age": 38},
    1002: {"name": "横山花子", "address": "千葉県銚子市", "age": 28},
    1004: {"name": "田中一郎", "address": "長野茅野市", "age": 48},
    1005: {"name": "星山裕子", "address": "福岡県太宰府市", "age": 33},
}

while True:
    number = int(input("社員番号(終了時は9999): "))
    if number == 9999:
        break
    if number in employees:
        employee = employees[number]
        print(f"名前: {employee['name']}")
        print(f"住所: {employee['address']}")
        print(f"年齢: {employee['age']}")
    else:
        print("該当する社員は存在しません。")