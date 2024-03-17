li = ["orange", "apple", "banana", "pineapple", "lemon", "apple", "banana"]

for index, fruit in enumerate(li):
    if fruit == "lemon":
        break
    
print(index)

def get_index_by_name(li, name):
    for index, item in enumerate(li):
        if item == name:
            return index
    return None

print(get_index_by_name(li, "lemon"))
print(get_index_by_name(li, "apple"))
print(get_index_by_name(li, "grape"))