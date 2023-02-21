import json, os

filepath = os.path.join(os.path.dirname(__file__), 'meibo.json')

with open(filepath, "r", encoding="utf_8") as f:
    json_obj = json.load(f)

for customer in sorted(json_obj['customers'], key=lambda c: c['pref']):
    print(f"{customer['name']} {customer['age']}歳 {customer['pref']}")
