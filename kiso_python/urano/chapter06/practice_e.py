import os, json

f = open(os.path.dirname(__file__) + '/meibo.json', 'r', encoding='utf_8')
json_obj = json.load(f)
sorted_customers = sorted(json_obj['customers'], key=lambda a:a['pref'])
for person in sorted_customers:
    print(f"{person['name']} {person['age']}歳 {person['pref']}")

print(ord('千'), ord('東'), ord('神'))