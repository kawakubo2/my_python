d1 = {'red': '赤', 'white': '白', 'yellow': '黄'}

d6 = dict(d1, blue='青', black='黒', white='しろ')

if 'yellow' in d6:
    pass
else:
    d6['yellow'] = '黄色'

if 'gray' in d6:
    print(d6['gray'])

print(d6)

a = [('博多区', 10, 3),('博多区', 20, 10),('博多区', 30, 7),('東区', 10, 1),
('東区', 20, 5),('東区', 30, 7)]

areas = ['博多区', '東区']
ages = [10, 20, 30]

area_count = {}
for area in areas:
    area_count[area] = 0

print(area_count)

for item in a:
    area_count[item[0]] += item[2] 

age_count = {}
for age in ages:
    age_count[age] = 0

for item in a:
    age_count[item[1]] += item[2]

print(age_count)

data = [{"area": "博多区", "age": 10, "infect": 3},{"area": "博多区", "age": 20, "infect": 5},
{"area": "博多区", "age": 10, "infect": 5},{"area": "博多区", "age": 20, "infect": 10}]

age_count2 = {}
for d in data:
    if d['age'] in age_count2:
        age_count2[d['age']] += d['infect']
    else:
        age_count2[d['age']] = d['infect']

print(age_count2)
