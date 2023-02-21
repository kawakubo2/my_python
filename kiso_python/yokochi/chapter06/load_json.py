import json, os

f = open(os.path.dirname(__file__) + '/meibo.json', 'r', encoding='utf_8')
json_obj = json.load(f)

for customer in sorted(json_obj['customers'], key=lambda c:c['age']):
    print(f"{customer['name']} {customer['age']}歳 {customer['pref']}")

f.close()