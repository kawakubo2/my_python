fruit_map = {"apple": 4, "grape": 3, "banana": 6}

# [4, 3, 6]
# ["apple", "grape", "banana"]

result = []
for val in fruit_map.values():
    result.append(val)
    
print(result)
    
result = []
for key in fruit_map.keys():
    result.append(key)
    
print(result)

amount = [val for _, val in fruit_map.items()]
print(amount)
fruit_names = [key for key, _ in fruit_map.items()]
print(fruit_names)

def keys_values(map):
    keys = []
    values = []
    for key, value in map.items():
        keys.append(key)
        values.append(value)
    return {"keys": keys, "values": values}

result = keys_values(fruit_map)
print(result["keys"])
print(result["values"])

fruit_map2 = {}
for name, quantity in zip(result["keys"], result["values"]):
    fruit_map2[name] = quantity
    
print(fruit_map2)