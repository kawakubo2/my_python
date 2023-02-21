import re

ss = ["7,564件", "123件", "23,456件"]
def extract_int(s):
    if "," in s:
        pattern = "^(([0-9]{1,3}),)+([0-9]{1,3})件$"
        ptn = re.compile(pattern)
        num = int(ptn.sub(r"\g<2>" + r"\g<3>", s))
    else:
        pattern = "^([0-9]{1,3})件$"
        ptn = re.compile(pattern)
        num = int(ptn.sub(r"\g<1>", s))
    return num

for s in ss:
    print(extract_int(s))
