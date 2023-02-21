import re

tel_pattern = '^([0-9]{2,4})-([0-9]{2,4})-([0-9]{4})$'

tel = '092-292-9999'

reg = re.compile(tel_pattern)

results = reg.search(tel)

print(results[0])
print(f"市外局番: {results[1]}")
print(f"市内局番: {results[2]}")
print(f"加入者番号: {results[3]}")