import json
import os

f = open(os.path.dirname(__file__) + '/meibo.json', 'r', encoding='utf_8')
json_obj = json.load(f)

sorted_customers = sorted(json_obj['customers'], key=lambda c:c['pref'])
for person in sorted_customers:
    print(f'{person["name"]} {person["age"]}歳 {person["pref"]}')
    
f.close()