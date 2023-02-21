import os, json
with open(os.path.dirname(__file__) + "/meibo.json", "r", encoding="UTF-8") as f:
    json_obj = json.load(f)
    print(json_obj)