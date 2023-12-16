colors = {"red": "赤", "blue": "青", "yellow": "黄色", "red": "あか"}
print(colors)
colors["green"] = "緑"
print(colors)
colors["red"] = "あかいろ"
print(colors)

fruits = {"banana": 5, "orange": 10, "grape": 5}
print(fruits["banana"])
print(fruits["orange"])
print(fruits["grape"])
if "banana" in fruits:
    fruits["banana"] += 10
print(fruits)
print(fruits["pear"])