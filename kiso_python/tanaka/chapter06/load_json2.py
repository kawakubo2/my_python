import os, json

file = os.path.join(os.path.dirname(__file__), "meibo.json")

with open(file, "r", encoding="utf_8") as f:
    json_obj = json.load(f)
    for person in json_obj['customers']:
        print(f"{person['name']} {person['age']}才 {person['pref']}")