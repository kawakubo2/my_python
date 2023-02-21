names = ["田中一郎:1979", "山田花子:2000", "井上太郎:1964",
         "藤本和雄:1988", "大津信:1959", "後藤信:1980"]

names.sort(key=lambda n: int(n[-4:]))
print(names)

members = [
    { "name": "山田太郎", "weight": 78, "height": 173},
    { "name": "横山花子", "weight": 53, "height": 150},
    { "name": "田中一郎", "weight": 78, "height": 180},
    { "name": "星山裕子", "weight": 54, "height": 165}
]

def bmi(member):
    return member['weight'] / (member['height'] / 100) ** 2

for member in sorted(members, key=lambda m: bmi(m)):
    print(f"{member['name']}:{bmi(member):.2f}")