str1 = 'abcdabdddddccdecdfaaabbcc'


dic1 = {}
for c in str1:
    if c in dic1:
        dic1[c] += 1
    else:
        dic1[c] = 1

for i, (c, cnt) in enumerate(sorted(dic1.items(), key=lambda t: t[1], reverse=True)):
    print('{}.{}:{}'.format(i+1, c, cnt))