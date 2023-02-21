import re

tel_pattern = re.compile('^(\d{2,4})-(\d{2,4})-(\d{4})$')
tel = '090-292-9999'
match1 = tel_pattern.search(tel)
if match1:
    print(f"電話番号: {match1.group(0)}")
    print(f"市外局番: {match1.group(1)}")
    print(f"市内局番: {match1.group(2)}")
    print(f"加入者番号: {match1.group(3)}")