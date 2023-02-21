dic = {"日": "Sun", "月": "Mon", "火": "Tue", "水": "Wed", "木": "Thu", "金": "Fri", "土": "Sat"}

for ja, en in dic.items():
    print(f"{ja}:{en}")
for t in dic.items():
    print(f"{t}")

members = [
    ("A101", 72, 180),("A110", 68, 172),("B230", 55, 162)
]

for member_no, weight, height in members:
    print(f"社員番号: {member_no} 体重: {weight}kg 身長: {height}cm")
for member in members:
    print(f"社員番号: {member[0]} 体重: {member[1]}kg 身長: {member[2]}cm")