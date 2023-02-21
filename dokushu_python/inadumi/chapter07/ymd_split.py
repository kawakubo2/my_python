import re

ptn = re.compile(r"[/\.-]")

result = ptn.split("2021-04-11")
if len(result) == 3:
    print(result)
result = ptn.split("2021/04/11")
if len(result) == 3:
    print(result)
result = ptn.split("2021.04.11")
if len(result) == 3:
    print(result)
result = ptn.split("2021/04-11")
if len(result) == 3:
    print(result)

s1 = "123, 456,   xyz,abc,lmn"
ptn = re.compile("\s*,\s*")
result = ptn.split(s1)
for r in result:
    print(f">{r}<")