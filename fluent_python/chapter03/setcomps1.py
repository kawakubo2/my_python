from unicodedata import name

set1 = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(set1)
set2 = {name(chr(i), '') for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(set2)
