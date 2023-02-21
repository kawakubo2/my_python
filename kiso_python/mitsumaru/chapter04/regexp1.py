import re

str1 = "私の実家の郵便番号は812-0013です。"

m = re.search("\\d{3}-\\d{4}", str1)

print(m.group())

print("Caf\u00E9")

print("私は今\nPythonを勉強しています。")

product_codes = ["A001", "A002", "E003", "E004", "E00005"]

for code in product_codes:
    m = re.search("^E..\\d$", code)
    if m:
        print(m.group())

words = ["fool", "pool", "poor", "loop", "pop", "lock", "pearl"]

for word in words:
    print(word)
    m = re.findall("o{2,}", word)
    if m:
        print(m)

tel_pattern = "\\d{2,4}-\\d{2,4}-\\d{4}"

str2 = "私のスマホの番号は090-1234-5678で、会社の固定は092-292-9999です"

m = re.findall(tel_pattern, str2)
print(m)