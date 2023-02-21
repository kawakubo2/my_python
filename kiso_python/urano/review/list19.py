list19 = [
    {'width': 7, 'height': 6},
    {'width': 5, 'height': 8},
    {'width': 9, 'height': 7},
    {'width': 3, 'height': 8},
    {'width': 4, 'height': 5},
]

# 42 40 63 24 20

total = 0
for rect in list19:
    total += rect['width'] * rect['height']
    print(f"{rect['width'] * rect['height']:4}", end="")
print(f"{total:5}")