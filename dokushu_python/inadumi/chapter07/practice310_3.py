import os, random
import re

print(abs(-12))
print(round(987.654, 2))

"""
PATH = os.path.dirname(__file__)
for file in os.listdir(PATH):
    path = os.path.join(PATH, file)
    if os.path.isdir(path):
        print('■' + file)
    elif os.path.isfile(path):
        print(f"□{file}({os.path.getsize(path)}byte)")
"""

def test(min, max, s):
    for i, n in enumerate(s):
        if i == 0:
            if min != n:
                return False
            last = n
            continue 
        if last + 1 != n:
            return False
        last = n
    return True
        


s = set()
for i in range(1000000):
    n = random.randrange(101)
    s.add(n)
    if n < 0 or n > 100:
        raise ValueError("範囲外")

for n in sorted(s):
    print(n)

print("合格" if test(0, 100, sorted(s)) else "不合格")

str1 = r"あああ/aaa\111/bbb\いいい@222\333/ccc"
ptn = re.compile(r"[\\/@]")
lst = ptn.split(str1)

for token in lst:
    print(token)