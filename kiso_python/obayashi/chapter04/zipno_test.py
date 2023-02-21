import re # Regular Expression(正規表現)

ptn = re.compile(r"^\d{3}-\d{4}$")

zip_nos = ["812-0013", "123-4567", "888-9999"]

for zip_no in zip_nos:
    result = ptn.search(zip_no)
    print(result.group())

s = "私の実家は812-0013、会社は123-4567です。引っ越す前は999-9999でした。携帯は090-1111-2222です。"
ptn2 = re.compile(r"\d{3}-\d{4}")

results = ptn2.findall(s)
for result in results:
    print(result)

digit_pattern = re.compile(r"^(\+|-)?\d+$")

numbers = [ "+1", "-1", "3", "+12", "-48", "77", "+18331", "-3852", "72981983"]

for num in numbers:
    m = digit_pattern.search(num)
    print(m.group())