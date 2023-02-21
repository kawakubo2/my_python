import os, json

filepath = os.path.join(os.path.dirname(__file__), 'meibo.json')

f = open(filepath, 'r', encoding='utf_8')
json_obj = json.load(f)

sorted_customers = sorted(json_obj['customers'], key=lambda c: c['pref'])
for customer in sorted_customers:
    print(f"{customer['name']} {customer['age']}歳 {customer['pref']}")

f.close()
