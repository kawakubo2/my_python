import json, os

f = open(os.path.dirname(__file__) + '/meibo.json', 'r', encoding='utf_8')
json_obj = json.load(f)

sorted_customers = sorted(json_obj['customers'], key=lambda a: a['pref'])
for person in sorted_customers:
    print(f"{person['name']}({person['pref']}) {person['age']}歳")

print(f"{ord('千')} < {ord('東')} < {ord('神')}")