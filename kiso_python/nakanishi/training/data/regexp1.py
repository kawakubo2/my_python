import re
s = input("文字列: ")
if len(re.findall("[A-Za-z-]*", s)) >= 0 and len(re.findall(r"\d+", s)) > 0 \
    and len(re.findall("[ぁ-んー]*", s)) >= 0 and len(re.findall("[ァ-ンー]*", s)) >= 0 \
    and len(re.findall("[一-鿐]+", s)) > 0:
    print(s)

help(rea)