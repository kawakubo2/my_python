import json, os

f = open(os.path.dirname(__file__) + '/meibo.json', 'r', encoding='utf_8')
json_obj = json.load(f)
print(type(json_obj))
customers = json_obj['customers']
print(type(customers))
for c in customers:
    print(type(c))
    print(f"{c['name']}({c['age']}) {c['pref']}")
f.close()