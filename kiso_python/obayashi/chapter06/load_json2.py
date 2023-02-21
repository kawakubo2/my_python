import os, json

with open(os.path.dirname(__file__) + "/meibo.json", "r", encoding="utf_8") as f:
    json_obj = json.load(f)
    for person in sorted(json_obj["Customers"], key=lambda a: a['age'], reverse=True):
        print(f"{person['name']} {person['age']}歳 {person['pref']}")