import re

s1 = "私の会社のURLはhttps://example.comです。";

pattern = re.compile(r"https?://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+")

print(pattern.sub(f'<a href="\g<0>">\g<0></a>', s1))