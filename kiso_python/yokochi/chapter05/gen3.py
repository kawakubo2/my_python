# gen3.py
str = "HeLlo"
gen = (c for c in str.upper())
print('1回目')
for c in gen:
    print(c)
print('2回目')
for c in gen:
    print(c)