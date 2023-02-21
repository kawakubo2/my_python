import re
m = re.search(r"^(\d{4})\s", "2021 大阪")
print(f">{m.group(1)}<")

m2 = re.search(r"(java)[^s]", "わかりやすいJavaオブジェクト指向編", re.IGNORECASE)
print(f"{m2.group(1)}")
