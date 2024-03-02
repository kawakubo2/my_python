def change_element_at(ls, index, elem):
    if not (0 <= index < len(ls)):
        raise ValueError(f"インデックスが範囲外です: {index}")
    ls[index] = elem

c = ["dog", "blue", "yellow"]

change_element_at(c, 0, "red")
print(c)

v = ["tomato", "pumpkin", "cucumber", "cabbege", "potato"]
change_element_at(v, 2, "onion")
print(v)