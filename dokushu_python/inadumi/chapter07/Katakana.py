name = "ヤマダタロウ"
# name = "ヤマダタロウA"

valid = True
for c in name:
    if ord(c) < 12449 or ord(c) > 12531:
        valid = False
        break

if valid:
    print('妥当')
else:
    print('妥当ではない')

print(ord('ァ'))
print(ord('ン'))
print(ord('A'))

import re

pattern = re.compile(r'^[ァ-ン]+$')
result = pattern.search(name)
if result:
    print(result.group(0))