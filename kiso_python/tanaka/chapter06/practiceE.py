import os, json

filepath = os.path.join(os.path.dirname(__file__), 'meibo.json')

f = open(filepath, 'r', encoding='utf_8')
json_obj = json.load(f)
print(json_obj)

sorted_customers = sorted(json_obj['customers'], key=lambda a: a['pref'])

for person in sorted_customers:
    print(f"{person['name']} {person['age']}才 {person['pref']}")

f.close()