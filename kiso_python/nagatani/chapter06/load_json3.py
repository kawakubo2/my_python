import os, json

def max_length(lst):
    max = len(lst[0]['name'])
    for item in lst:
        if len(item['name']) > max:
            max = len(item['name'])
    return max

f = open(os.path.dirname(__file__) + "/meibo.json", "r", encoding="utf_8")
json_obj = json.load(f)

sorted_customers = sorted(json_obj["customers"], key=lambda a: a["age"])
for person in sorted_customers:
    print(f"{person['name']:{max_length(sorted_customers)}} {person['age']}歳　{person['pref']}")

f.close()