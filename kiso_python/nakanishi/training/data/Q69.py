def get_elem_at(li, index):
    if not (0 <= index <len(li)):
        raise ValueError(f"インデックスが範囲外: {index}")
    return li[index]

li = [1, 2, 3, 4, 5]
print(get_elem_at(li, 2))

c = ["dog", "blue", "yellow"]
print(get_elem_at(c, 2))

v = ["tomato", "pumpkin", "cucumber", "cabbege", "potato"]
print(get_elem_at(v, 1))