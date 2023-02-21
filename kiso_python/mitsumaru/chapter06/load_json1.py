import os, json

with open(os.path.dirname(__file__) + "/meibo.json", "r", encoding="utf_8") as f:
    json_obj = json.load(f)
    print(json_obj)