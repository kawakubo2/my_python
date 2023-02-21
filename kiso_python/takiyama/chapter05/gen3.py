s = 'HeLlo'

gen = (c for c in s.upper())
for c in gen:
    print(c)