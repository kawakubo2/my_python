import os, json

f = open(os.path.dirname(__file__) + '/meibo.json', 'r', encoding='utf_8')
json_obj = json.load(f)

for person in json_obj['customers']:
    print(f"{person['name']} {person['age']}歳 {person['pref']}")


f.close()