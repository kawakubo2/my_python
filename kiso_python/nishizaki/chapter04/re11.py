import re

# pattern = "^([0-9]{2,4})-([0-9]{2,4})-([0-9]{4})$"
pattern = "^(\d{2,4})-(\d{2,4})-(\d{4})$"
tel = "092-272-9999"
m = re.search(pattern, tel)

if m:
    print(f"市外局番: {m.group(1)}")
    print(f"市内局番: {m.group(2)}")
    print(f"加入者番号: {m.group(3)}")

url1 = 'https://haru-idea.jp'
url2 = 'http://example.com'

url_pattern = "^https?://"

if re.search(url_pattern, url1):
    print(f"{url1}はURLです")

if re.search(url_pattern, url2):
    print(f"{url2}はURLです")
    
pattern1 = "(ワイン|ケーキ|チーズ)(が|も|は)好き"

a1 = ["ワインが好き", "ワインも好き", "ケーキが好き", "ケーキも好き"]
for s in a1:
    if re.search(pattern1, s):
        print(s)