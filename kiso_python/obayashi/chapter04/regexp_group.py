import re

pattern = re.compile('^(\d{2,4})-(\d{2,4})-(\d{4})$')

tels = ['092-292-9999', '03-3721-0564', '045-777-0000']

for tel in tels:
    results = pattern.finditer(tel)
    for result in results:
        print(f"固定電話:{result.group()}")
        print(f"市外局番:{result.group(1)}")
        print(f"市内局番:{result.group(2)}")
        print(f"加入者番号:{result.group(3)}")
        print('-----------------')