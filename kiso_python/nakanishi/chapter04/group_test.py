import re

m = re.search(r"^(\d{2,4})-(\d{2,4})-(\d{4})$", "092-292-9999")
print(f"固定電話番号: {m.group()}")
print(f"市外局番: {m.group(1)}")
print(f"市内局番: {m.group(2)}")
print(f"加入者番号: {m.group(3)}")