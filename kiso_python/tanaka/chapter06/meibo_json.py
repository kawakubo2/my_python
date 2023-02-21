import json, os

file = os.path.join(os.path.dirname(__file__), "meibo.json")
with open(file, "r", encoding="utf_8") as f:
    json_obj = json.load(f)
    print(json_obj)