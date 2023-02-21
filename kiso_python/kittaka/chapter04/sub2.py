import re

s = "私の教室はhttps://haru-idea.jpです。"

pattern = r"http(s)?://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+"
reg = re.compile(pattern)

print(reg.sub(r'<a href="\g<0>">\g<0></a>', s))