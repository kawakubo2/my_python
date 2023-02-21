import os, json

filepath = os.path.join(os.path.dirname(__file__), 'meibo.json')
f = open(filepath, "r", encoding="utf_8")
json_obj = json.load(f)

for customer in sorted(json_obj["customers"], key=lambda c: c['age']):
    print("----------------------")
    print(f"名前: {customer['name']}")
    print(f"年齢: {customer['age']}")
    print(f"都道府県名: {customer['pref']}")