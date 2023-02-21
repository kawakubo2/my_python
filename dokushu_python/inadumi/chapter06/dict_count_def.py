from collections import defaultdict, OrderedDict

data = ['太郎', '花子', '次郎', '太郎', '太郎', '太郎', '花子', '花子', '花子', '花子']

result = defaultdict(int)
print(result)

for key in data:
    result[key] += 1

dict2 = OrderedDict()

for name, num in sorted(result.items(), key=lambda p: p[1], reverse=True):
    dict2[name] = num

print(dict2)

