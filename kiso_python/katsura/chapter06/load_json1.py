import json, os

f = open(os.path.dirname(__file__) + '/meibo.json', 'r', encoding='utf_8')
json_obj = json.load(f)
print(json_obj)
f.close()