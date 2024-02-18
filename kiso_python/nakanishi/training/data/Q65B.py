colors = ["red", "blue", "yellow"]
fruits = ["banana", "apple", "orange", "grape", "strawberry"]

def get_element_at(items, index):
    if not (0 <= index < len(items)):
        raise ValueError("インデックが範囲外です。")
    return items[index]

try:
    print(get_element_at(colors, 2))
    print(get_element_at(fruits, 3))
    print(get_element_at(fruits, 5))
except ValueError as e:
    print(e)
