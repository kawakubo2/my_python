s = '日月火水木金土';
weeks = []
for c in s:
    weeks.append(c + '曜日')

print(weeks)

print(weeks[0])
print(weeks[1])
print(weeks[2])
print(weeks[3])
print(weeks[4])
print(weeks[5])
print(weeks[6])

print('----')
for w in weeks:
    print(w)
print('----')
weeks.reverse()
for w in weeks:
    print(w)